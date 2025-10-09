"""Production-grade async PDF to Markdown processor - Ultimate Edition.

This script consolidates the best features from all previous versions into a single,
robust, high-performance solution optimized for processing millions of PDFs.

Key Features:
1. Async/await for maximum throughput (from async.py)
2. Dual worker pools for download vs processing (from optimized.py)
3. Graceful shutdown and signal handling (from robust.py)
4. Per-file process isolation and timeout (from enhanced retry)
5. Checkpointing and resume capability (from robust.py)
6. Batch processing for memory efficiency (new)
7. Multiple parser fallbacks (from enhanced retry)
8. Pre-processing validation (from enhanced retry)
9. Comprehensive error reporting (from all)
10. Performance metrics and monitoring (from optimized.py)

Optimizations for Millions of Files:
- Batched processing (100-1000 files per batch)
- Aggressive garbage collection
- Memory health checks
- Progress checkpointing every 50 files
- Graceful shutdown with state saving
- Resume from last checkpoint
- Connection pooling
- Rate limiting and backpressure

Run with:
    # Default: Process all new files
    uv run python SimpleWorkflow/pdf_processor.py

    # Custom workers
uv run python SimpleWorkflow/pdf_processor.py --download-workers 30 --processing-workers 10

    # Process with batching (for millions of files)
    uv run python SimpleWorkflow/pdf_processor.py \\
        --batch-size 1000 --checkpoint-interval 100

    # Resume after interruption
    uv run python SimpleWorkflow/pdf_processor.py --resume

    # Retry only failed files
    uv run python SimpleWorkflow/pdf_processor.py --retry-failed

Features:
- Scales to millions of files
- Graceful shutdown (Ctrl+C, SIGTERM)
- Auto-resume from crashes
- Per-file isolation prevents cascade failures
- Multiple extraction strategies
- Comprehensive monitoring
"""

# %%
from __future__ import annotations

import asyncio
import gc
import json
import logging
import os
import resource
import signal
import sys
import tempfile
import time
import traceback
import zipfile
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeoutError
from dataclasses import asdict, dataclass, field
from datetime import datetime
from io import BytesIO
from pathlib import Path
from typing import Any, Optional

import aioboto3
import pandas as pd
import psutil
from dotenv import load_dotenv
from tqdm.asyncio import tqdm

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from localPDFparse.parse import DocumentMetadata, ExtractionQuality, extract_markdown
from s3pdf_manager.download_pdf import (
    S3Config,
    _looks_like_pdf,
    _resolve_bucket_and_key,
    _sanitize_filename_component,
    load_metadata,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s | PID:%(process)d",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("SimpleWorkflow/pdf_processor.log", mode="a"),
    ],
)
logger = logging.getLogger(__name__)

# Suppress verbose logging
for lib in ["boto3", "botocore", "aiobotocore", "urllib3", "s3transfer"]:
    logging.getLogger(lib).setLevel(logging.WARNING)

# Load environment variables
load_dotenv()

# Constants
METADATA_PATH = "sql/metadata_table/flora_fauna_metadata_indexed.parquet"
OUTPUT_DIR = Path("SimpleWorkflow/ParsedFiles")
TEMP_DIR = Path(tempfile.gettempdir()) / "pdf_processor"
STATE_FILE = Path("SimpleWorkflow/.pdf_processor_state.json")
MAX_RETRIES = 3
RETRY_DELAY = 1
PDF_TIMEOUT_SECONDS = 300  # 5 minutes per PDF
MEMORY_LIMIT_GB = 2  # 2GB per process
BATCH_SIZE = 100  # Process files in batches
CHECKPOINT_INTERVAL = 50  # Save progress every N files
MEMORY_THRESHOLD_PERCENT = 85  # Trigger GC at this percentage


# Auto-detect optimal workers
def get_optimal_workers() -> tuple[int, int]:
    """Calculate optimal number of download and processing workers."""
    cpu_count = os.cpu_count() or 4
    memory_gb = psutil.virtual_memory().total / (1024**3)

    # Download workers: I/O bound (can be 2-3x CPU count)
    download_workers = min(cpu_count * 3, int(memory_gb * 2), 30)

    # Processing workers: CPU and memory intensive
    processing_workers = min(max(cpu_count - 1, 2), int(memory_gb / 2), 12)

    return download_workers, processing_workers


DEFAULT_DOWNLOAD_WORKERS, DEFAULT_PROCESSING_WORKERS = get_optimal_workers()


# Global flag for graceful shutdown
shutdown_requested = False


def signal_handler(signum, frame):
    """Handle shutdown signals gracefully."""
    global shutdown_requested
    if not shutdown_requested:
        logger.info("")
        logger.info("=" * 70)
        logger.info("🛑 Shutdown signal received (SIGTERM/SIGINT)")
        logger.info("=" * 70)
        logger.info("Completing current tasks and saving checkpoint...")
        logger.info("Press Ctrl+C again to force quit (not recommended)")
        shutdown_requested = True
    else:
        logger.warning("⚠️  Force shutdown requested!")
        sys.exit(1)


# Register signal handlers
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)


@dataclass
class PerformanceMetrics:
    """Track comprehensive performance metrics."""

    start_time: float = field(default_factory=time.time)
    download_times: list[float] = field(default_factory=list)
    processing_times: list[float] = field(default_factory=list)
    total_bytes_downloaded: int = 0
    memory_samples: list[float] = field(default_factory=list)
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def add_download_time(self, duration: float, bytes_count: int):
        async with self.lock:
            self.download_times.append(duration)
            self.total_bytes_downloaded += bytes_count

    async def add_processing_time(self, duration: float):
        async with self.lock:
            self.processing_times.append(duration)

    async def sample_memory(self):
        async with self.lock:
            memory_mb = psutil.Process().memory_info().rss / 1024 / 1024
            self.memory_samples.append(memory_mb)

    def get_summary(self) -> dict:
        """Get performance summary."""
        elapsed = time.time() - self.start_time
        return {
            "total_time": elapsed,
            "avg_download_time": (
                sum(self.download_times) / len(self.download_times)
                if self.download_times
                else 0
            ),
            "avg_processing_time": (
                sum(self.processing_times) / len(self.processing_times)
                if self.processing_times
                else 0
            ),
            "total_mb_downloaded": self.total_bytes_downloaded / (1024 * 1024),
            "download_speed_mbps": (
                (self.total_bytes_downloaded / (1024 * 1024)) / elapsed
                if elapsed > 0
                else 0
            ),
            "avg_memory_mb": (
                sum(self.memory_samples) / len(self.memory_samples)
                if self.memory_samples
                else 0
            ),
            "peak_memory_mb": max(self.memory_samples) if self.memory_samples else 0,
        }


@dataclass
class ProcessingStats:
    """Track processing statistics with async-safe operations."""

    total: int = 0
    processed: int = 0
    skipped: int = 0
    failed: int = 0
    validation_failed: int = 0
    timeout_failed: int = 0
    fallback_used: int = 0
    errors: list[tuple[str, str, str]] = field(
        default_factory=list
    )  # (file_id, error_type, error_msg)
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def increment_processed(self):
        async with self.lock:
            self.processed += 1

    async def increment_skipped(self):
        async with self.lock:
            self.skipped += 1

    async def increment_failed(self, idx: str, error_type: str, error_msg: str):
        async with self.lock:
            self.failed += 1
            self.errors.append((idx, error_type, error_msg))

            # Categorize
            error_lower = error_msg.lower()
            if "validation" in error_lower:
                self.validation_failed += 1
            elif "timeout" in error_lower:
                self.timeout_failed += 1

    async def increment_fallback_used(self):
        async with self.lock:
            self.fallback_used += 1

    def log_summary(self):
        """Log comprehensive processing summary."""
        logger.info("=" * 70)
        logger.info("PROCESSING SUMMARY")
        logger.info("=" * 70)
        logger.info("")
        logger.info("📈 Results:")
        logger.info("   Total files:      %d", self.total)
        logger.info("   ✓ Processed:      %d", self.processed)
        logger.info("   ⏭ Skipped:        %d", self.skipped)
        logger.info("   ✗ Failed:         %d", self.failed)

        if self.total > 0:
            success_rate = self.processed / self.total * 100
            logger.info("   Success Rate:    %.1f%%", success_rate)

        logger.info("")
        logger.info("🔧 Strategy Stats:")
        logger.info("   Fallback Used:    %d", self.fallback_used)
        logger.info("   Validation Failed: %d", self.validation_failed)
        logger.info("   Timeout Failed:   %d", self.timeout_failed)
        logger.info("")


@dataclass
class ProcessingState:
    """Track processing state for resume capability."""

    total_files: int = 0
    processed_files: list[str] = field(default_factory=list)
    successful_files: list[str] = field(default_factory=list)
    failed_files: list[str] = field(default_factory=list)
    start_time: str = field(default_factory=lambda: datetime.now().isoformat())
    last_checkpoint: str = field(default_factory=lambda: datetime.now().isoformat())
    current_batch: int = 0

    def save(self, path: Path) -> None:
        """Save state to file."""
        self.last_checkpoint = datetime.now().isoformat()
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(asdict(self), f, indent=2)

    @classmethod
    def load(cls, path: Path) -> Optional[ProcessingState]:
        """Load state from file."""
        if not path.exists():
            return None
        try:
            with open(path, "r") as f:
                data = json.load(f)
            return cls(**data)
        except Exception as e:
            logger.warning("Could not load state from %s: %s", path, e)
            return None


def ensure_directories():
    """Ensure required directories exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)


def parse_failed_file_metadata(failed_file_path: Path) -> Optional[dict]:
    """Parse metadata from a FAILED-*.md file using YAML parser.

    Returns:
        Dictionary with file_identifier, s3_key, and error info, or None.
    """
    try:
        import yaml as yaml_parser

        content = failed_file_path.read_text(encoding="utf-8", errors="ignore")

        # Try to parse YAML frontmatter
        if content.startswith("---"):
            yaml_end = content.find("---", 3)
            if yaml_end > 0:
                yaml_content = content[3:yaml_end].strip()
                metadata = yaml_parser.safe_load(yaml_content)

                if isinstance(metadata, dict):
                    if "file_identifier" in metadata and "s3_key" in metadata:
                        return metadata

        # Fallback: parse line by line
        lines = content.split("\n")
        metadata = {}
        in_frontmatter = False

        for line in lines:
            if line.strip() == "---":
                if not in_frontmatter:
                    in_frontmatter = True
                else:
                    break
                continue

            if in_frontmatter and ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip()

        if "file_identifier" in metadata and "s3_key" in metadata:
            return metadata

        return None
    except Exception as exc:
        logger.error("Failed to parse %s: %s", failed_file_path, exc)
        return None


def find_failed_files_for_retry(output_dir: Path = OUTPUT_DIR) -> list[str]:
    """Find all FAILED-*.md files and extract their file identifiers.

    Args:
        output_dir: Directory to search for FAILED-*.md files

    Returns:
        List of file identifiers from FAILED files
    """
    failed_ids = []

    for failed_path in output_dir.glob("FAILED-*.md"):
        metadata = parse_failed_file_metadata(failed_path)
        if metadata and "file_identifier" in metadata:
            failed_ids.append(metadata["file_identifier"])
            logger.debug(
                "Found FAILED file: %s (error: %s)",
                metadata["file_identifier"],
                metadata.get("error", "unknown")[:50],
            )
        else:
            # Fallback: try to extract from content
            try:
                content = failed_path.read_text()
                for line in content.split("\n"):
                    if line.startswith("file_identifier:"):
                        file_id = line.split(":", 1)[1].strip()
                        failed_ids.append(file_id)
                        break
            except Exception as e:
                logger.warning("Could not parse %s: %s", failed_path, e)

    return failed_ids


def _extract_pdf_from_zip_bytes(
    zip_bytes: bytes, prefer_name: Optional[str] = None
) -> tuple[str, bytes]:
    """Extract a PDF file from ZIP archive bytes."""
    with zipfile.ZipFile(BytesIO(zip_bytes), "r") as zf:
        pdf_files = [
            name
            for name in zf.namelist()
            if name.lower().endswith(".pdf") and not name.startswith("__MACOSX")
        ]

        if not pdf_files:
            raise ValueError("No PDF files found in ZIP archive")

        if prefer_name and prefer_name in pdf_files:
            selected_pdf = prefer_name
        elif len(pdf_files) == 1:
            selected_pdf = pdf_files[0]
        else:
            sizes = {name: zf.getinfo(name).file_size for name in pdf_files}
            selected_pdf = max(sizes, key=sizes.get)

        return selected_pdf, zf.read(selected_pdf)


def validate_pdf_before_processing(
    pdf_bytes: bytes, file_identifier: str
) -> tuple[bool, str]:
    """Validate PDF before attempting extraction."""
    # Check magic bytes
    if not pdf_bytes.startswith(b"%PDF"):
        if pdf_bytes.startswith(b"\xef\xbb\xbf"):  # UTF-8 BOM
            pdf_bytes = pdf_bytes[3:]
            if not pdf_bytes.startswith(b"%PDF"):
                return False, "Invalid PDF magic bytes (even after BOM removal)"
        else:
            return (
                False,
                f"Invalid PDF magic bytes (starts with: {pdf_bytes[:20]!r})",
            )

    # Check file size
    size_mb = len(pdf_bytes) / (1024 * 1024)
    if size_mb < 0.001:
        return False, f"File too small ({size_mb:.6f}MB)"
    if size_mb > 500:
        logger.warning("%s: Very large file (%.1fMB)", file_identifier, size_mb)

    # Try to open with PyMuPDF (lightweight check)
    try:
        import pymupdf

        temp_path = Path(tempfile.mktemp(suffix=".pdf"))
        try:
            temp_path.write_bytes(pdf_bytes)
            doc = pymupdf.open(temp_path)
            page_count = len(doc)
            doc.close()

            if page_count == 0:
                return False, "PDF has 0 pages"
            if page_count > 10000:
                logger.warning(
                    "%s: Very long PDF (%d pages)", file_identifier, page_count
                )

            return True, ""
        finally:
            if temp_path.exists():
                temp_path.unlink()
    except Exception as e:
        return False, f"PDF validation failed: {type(e).__name__}: {str(e)}"


def _extract_markdown_with_pymupdf(pdf_path_str: str) -> tuple[str, Any]:
    """Extract using PyMuPDF (primary method)."""
    return extract_markdown(
        pdf_path_str,
        output_dir=None,
        ignore_images=True,
        clean_text=True,
        validate_quality=True,
        show_progress=False,
    )


def verify_extraction_dependencies():
    """Verify all PDF extraction libraries are available at startup."""
    import sys

    missing = []
    available = []

    try:
        import pymupdf

        available.append(f"pymupdf ({pymupdf.__version__})")
    except ImportError:
        missing.append("pymupdf")

    try:
        import pdfplumber

        available.append(f"pdfplumber ({pdfplumber.__version__})")
    except ImportError:
        missing.append("pdfplumber")

    try:
        import pypdf

        available.append(f"pypdf ({pypdf.__version__})")
    except ImportError:
        missing.append("pypdf")

    logger.info("=" * 70)
    logger.info("ENVIRONMENT VERIFICATION")
    logger.info("=" * 70)
    logger.info("Python executable: %s", sys.executable)

    if available:
        logger.info("✓ Available PDF libraries:")
        for lib in available:
            logger.info("  - %s", lib)

    if missing:
        logger.warning("⚠ Missing PDF libraries:")
        for lib in missing:
            logger.warning("  - %s", lib)
        logger.warning("")
        logger.warning(
            "Some extraction strategies will not be available. Install with: uv add %s",
            " ".join(missing),
        )

        # Don't fail if at least one library is available
        if not available:
            raise EnvironmentError(
                "No PDF extraction libraries available. "
                "Install with: uv add pymupdf pdfplumber pypdf"
            )
    else:
        logger.info("✓ All PDF extraction libraries available")

    logger.info("=" * 70)
    logger.info("")


def _extract_markdown_with_pdfplumber(pdf_path_str: str) -> tuple[str, Any]:
    """Extract using pdfplumber (fallback)."""
    # Let ImportError propagate as normal exception to allow pypdf fallback
    import pdfplumber

    with pdfplumber.open(pdf_path_str) as pdf:
        pages_text = []
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            if text:
                pages_text.append(f"## Page {page_num}\n\n{text}")

        combined_text = "\n\n---\n\n".join(pages_text)
        metadata = DocumentMetadata(
            page_count=len(pdf.pages),
            extraction_quality=ExtractionQuality.MEDIUM,
            quality_notes=["pdfplumber fallback used"],
        )
        return combined_text, metadata


def _extract_markdown_with_pypdf(pdf_path_str: str) -> tuple[str, Any]:
    """Extract using pypdf (last resort fallback)."""
    # Let ImportError propagate as normal exception
    from pypdf import PdfReader

    reader = PdfReader(pdf_path_str)
    pages_text = []

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            pages_text.append(f"## Page {page_num}\n\n{text}")

    combined_text = "\n\n---\n\n".join(pages_text)
    metadata = DocumentMetadata(
        page_count=len(reader.pages),
        extraction_quality=ExtractionQuality.LOW,
        quality_notes=["pypdf fallback used"],
    )
    return combined_text, metadata


def _extract_markdown_worker_isolated(
    pdf_path_str: str,
) -> tuple[str, Any, dict]:
    """Extract markdown in isolated worker with all strategies and resource limits."""
    import sys

    stats = {"fallback_used": False, "strategy": "pymupdf"}

    # Verify we're in the correct environment
    logger.debug("Worker Python executable: %s", sys.executable)

    # Check library availability (log warnings but don't fail yet)
    available_libs = []
    try:
        import pymupdf

        available_libs.append("pymupdf")
    except ImportError:
        logger.warning("pymupdf not available in worker process")

    try:
        import pdfplumber

        available_libs.append("pdfplumber")
    except ImportError:
        logger.warning("pdfplumber not available in worker process")

    try:
        import pypdf

        available_libs.append("pypdf")
    except ImportError:
        logger.warning("pypdf not available in worker process")

    if not available_libs:
        raise EnvironmentError(
            f"No PDF extraction libraries available in worker. "
            f"Python: {sys.executable}. "
            f"This indicates an environment configuration issue."
        )

    logger.debug("Available PDF libraries in worker: %s", ", ".join(available_libs))

    # Set memory limit
    try:
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        resource.setrlimit(
            resource.RLIMIT_AS, (MEMORY_LIMIT_GB * 1024 * 1024 * 1024, hard)
        )
    except Exception as e:
        logger.debug("Could not set memory limit: %s", e)

    # Force garbage collection
    gc.collect()

    try:
        # Strategy 1: PyMuPDF (primary)
        result = _extract_markdown_with_pymupdf(pdf_path_str)
        return (*result, stats)

    except Exception as pymupdf_error:
        # Strategy 2: pdfplumber
        logger.info("PyMuPDF failed, trying pdfplumber fallback...")
        try:
            stats["fallback_used"] = True
            stats["strategy"] = "pdfplumber"
            result = _extract_markdown_with_pdfplumber(pdf_path_str)
            return (*result, stats)
        except Exception as pdfplumber_error:
            # Strategy 3: pypdf
            logger.info("pdfplumber failed, trying pypdf fallback...")
            try:
                stats["fallback_used"] = True
                stats["strategy"] = "pypdf"
                result = _extract_markdown_with_pypdf(pdf_path_str)
                return (*result, stats)
            except Exception as pypdf_error:
                raise RuntimeError(
                    f"All extraction strategies failed. "
                    f"PyMuPDF: {pymupdf_error}, "
                    f"pdfplumber: {pdfplumber_error}, "
                    f"pypdf: {pypdf_error}"
                )

    finally:
        gc.collect()


def extract_markdown_with_isolation(pdf_path_str: str) -> tuple[str, Any, dict]:
    """Extract markdown with per-file process isolation and timeout."""
    with ProcessPoolExecutor(max_workers=1) as isolated_executor:
        future = isolated_executor.submit(
            _extract_markdown_worker_isolated, pdf_path_str
        )

        try:
            result = future.result(timeout=PDF_TIMEOUT_SECONDS)
            return result

        except FuturesTimeoutError:
            logger.error(
                "Timeout processing %s after %ds", pdf_path_str, PDF_TIMEOUT_SECONDS
            )
            isolated_executor.shutdown(wait=False, cancel_futures=True)
            raise TimeoutError(
                f"PDF processing exceeded {PDF_TIMEOUT_SECONDS}s timeout"
            )

        except Exception as e:
            logger.error("Error processing %s: %s", pdf_path_str, e)
            raise


async def download_from_s3_async(
    session: aioboto3.Session,
    bucket: str,
    s3_key: str,
    metrics: PerformanceMetrics,
    max_retries: int = MAX_RETRIES,
) -> bytes:
    """Download file from S3 asynchronously with retries and metrics."""
    start_time = time.time()

    for attempt in range(max_retries):
        try:
            async with session.client("s3") as s3_client:
                response = await s3_client.get_object(Bucket=bucket, Key=s3_key)
                content = await response["Body"].read()

                duration = time.time() - start_time
                await metrics.add_download_time(duration, len(content))
                return content

        except Exception as e:
            if attempt < max_retries - 1:
                logger.debug(
                    "Download attempt %d/%d failed: %s", attempt + 1, max_retries, e
                )
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))
            else:
                raise


async def process_pdf_async(
    pdf_bytes: bytes,
    file_identifier: str,
    metrics: PerformanceMetrics,
) -> tuple[bool, str, Optional[str], dict]:
    """Process PDF bytes to markdown with isolation and all safety measures."""
    start_time = time.time()
    temp_dir = TEMP_DIR
    temp_dir.mkdir(parents=True, exist_ok=True)

    safe_name = _sanitize_filename_component(file_identifier)
    temp_pdf_path = temp_dir / f"{safe_name}.pdf"

    try:
        # Write PDF to temp file
        temp_pdf_path.write_bytes(pdf_bytes)

        # Extract markdown using isolated process with timeout
        loop = asyncio.get_event_loop()
        markdown, metadata, stats = await loop.run_in_executor(
            None,
            extract_markdown_with_isolation,
            str(temp_pdf_path),
        )

        duration = time.time() - start_time
        await metrics.add_processing_time(duration)

        return True, markdown, None, stats

    except Exception as exc:
        error_type = type(exc).__name__
        error_msg = str(exc)
        return False, "", f"{error_type}: {error_msg}", {}
    finally:
        if temp_pdf_path.exists():
            try:
                temp_pdf_path.unlink()
            except Exception:
                pass


def save_error_markdown(
    index_value: str,
    error: Exception,
    row: pd.Series,
    s3_key: str = None,
) -> None:
    """Save comprehensive error report."""
    safe_index = _sanitize_filename_component(index_value)
    error_path = OUTPUT_DIR / f"FAILED-{safe_index}.md"

    error_content = f"""---
file_identifier: {index_value}
status: FAILED
error_type: {type(error).__name__}
error_time: {datetime.now().isoformat()}
s3_key: {s3_key or "N/A"}
nombre: {row.get("nombre", "N/A")}
fecha_presentacion: {row.get("fecha_de_presentacion", "N/A")}
region: {row.get("region", "N/A")}
tipo_proyecto: {row.get("tipo_de_proyecto", "N/A")}
---

# Processing Failed

## Error Details

**Error Type:** `{type(error).__name__}`

**Error Message:**
```
{str(error)}
```

## Full Traceback
```python
{traceback.format_exc()}
```

## Metadata Information

- **File Identifier:** {index_value}
- **S3 Key:** {s3_key or "Could not resolve"}
- **From Compressed:** {row.get("from_compressed_file", "N/A")}
- **File Name:** {row.get("file_name", "N/A")}
- **URL:** {row.get("url", "N/A")}

---
*Generated by PDF Processor v2.0*
"""

    try:
        error_path.write_text(error_content, encoding="utf-8")
    except Exception as e:
        logger.error("Failed to save error report for %s: %s", index_value, e)


async def process_single_pdf(
    session: aioboto3.Session,
    row: pd.Series,
    idx: str,
    stats: ProcessingStats,
    metrics: PerformanceMetrics,
    state: ProcessingState,
    skip_existing: bool = True,
    retry_mode: bool = False,
) -> None:
    """Process a single PDF with all optimizations and safety measures."""
    global shutdown_requested

    if shutdown_requested:
        return

    safe_idx = _sanitize_filename_component(idx)
    markdown_path = OUTPUT_DIR / f"{safe_idx}.md"
    error_path = OUTPUT_DIR / f"FAILED-{safe_idx}.md"

    # Skip logic depends on mode
    if skip_existing:
        if retry_mode:
            # In retry mode: only skip if success file exists (allow reprocessing FAILED)
            if markdown_path.exists():
                await stats.increment_skipped()
                return
        else:
            # Normal mode: skip if either success or error file exists
            if markdown_path.exists() or error_path.exists():
                await stats.increment_skipped()
                return

    s3_key = None

    try:
        # Resolve S3 location
        bucket, s3_key = _resolve_bucket_and_key(row)

        # Skip system files
        if "__MACOSX" in s3_key or "/._" in s3_key or s3_key.startswith("._"):
            await stats.increment_skipped()
            return

        # Download from S3
        content = await download_from_s3_async(session, bucket, s3_key, metrics)

        # Check if it's from a compressed file
        from_zip = bool(row.get("from_compressed_file", False))

        if from_zip:
            if _looks_like_pdf(content):
                pdf_bytes = content
            else:
                prefer_name = row.get("file_name")
                _, pdf_bytes = _extract_pdf_from_zip_bytes(content, prefer_name)
        else:
            pdf_bytes = content

        # Remove UTF-8 BOM if present
        if pdf_bytes.startswith(b"\xef\xbb\xbf"):
            pdf_bytes = pdf_bytes[3:]

        # Validate PDF
        is_valid, validation_error = validate_pdf_before_processing(pdf_bytes, idx)
        if not is_valid:
            raise ValueError(f"PDF validation failed: {validation_error}")

        # Process PDF
        success, markdown_content, error_msg, proc_stats = await process_pdf_async(
            pdf_bytes, idx, metrics
        )

        if not success:
            raise RuntimeError(f"Extraction failed: {error_msg}")

        # Track fallback usage
        if proc_stats.get("fallback_used"):
            await stats.increment_fallback_used()

        # Add metadata header
        header = f"""---
file_identifier: {idx}
s3_key: {s3_key}
nombre: {row.get("nombre", "N/A")}
fecha_presentacion: {row.get("fecha_de_presentacion", "N/A")}
region: {row.get("region", "N/A")}
tipo_proyecto: {row.get("tipo_de_proyecto", "N/A")}
extraction_strategy: {proc_stats.get("strategy", "unknown")}
processing_time: {datetime.now().isoformat()}
---

"""
        full_markdown = header + markdown_content
        full_markdown = full_markdown.encode("utf-8", errors="ignore").decode("utf-8")

        # Save markdown
        markdown_path.write_text(full_markdown, encoding="utf-8")
        await stats.increment_processed()

        # Update state
        state.successful_files.append(idx)
        state.processed_files.append(idx)

        # Clean up FAILED file if exists (successful retry)
        if error_path.exists():
            try:
                error_path.unlink()
                logger.debug(
                    "Removed FAILED file after successful retry: %s", error_path.name
                )
            except Exception as e:
                logger.warning("Could not delete FAILED file %s: %s", error_path, e)

        logger.info("✓ %s (strategy: %s)", idx, proc_stats.get("strategy", "unknown"))

    except Exception as exc:
        error_type = type(exc).__name__
        error_msg = str(exc)
        await stats.increment_failed(idx, error_type, error_msg)

        # Save error report
        save_error_markdown(idx, exc, row, s3_key)

        # Update state
        state.failed_files.append(idx)
        state.processed_files.append(idx)

        logger.debug("✗ %s: %s: %s", idx, error_type, error_msg)


async def process_batch_async(
    df: pd.DataFrame,
    indices: Optional[list[str]] = None,
    max_files: Optional[int] = None,
    skip_existing: bool = True,
    retry_failed: bool = False,
    download_workers: int = DEFAULT_DOWNLOAD_WORKERS,
    processing_workers: int = DEFAULT_PROCESSING_WORKERS,
    batch_size: int = BATCH_SIZE,
    checkpoint_interval: int = CHECKPOINT_INTERVAL,
    resume: bool = True,
) -> tuple[ProcessingStats, PerformanceMetrics, ProcessingState]:
    """Process PDFs asynchronously with all optimizations.

    Optimized for millions of files with:
    - Batched processing for memory efficiency
    - Checkpointing for resume capability
    - Graceful shutdown handling
    - Per-file isolation
    - Multiple extraction strategies
    """
    stats = ProcessingStats()
    metrics = PerformanceMetrics()
    global shutdown_requested

    # Load or create state
    state = None
    if resume and STATE_FILE.exists():
        state = ProcessingState.load(STATE_FILE)
        if state:
            logger.info("📂 Resuming from checkpoint:")
            logger.info("   Previously processed: %d files", len(state.processed_files))
            logger.info("   Previous successes: %d", len(state.successful_files))
            logger.info("   Previous failures: %d", len(state.failed_files))

    if state is None:
        state = ProcessingState()
        state.start_time = datetime.now().isoformat()

    # Determine indices to process
    if retry_failed:
        # Find FAILED-*.md files using robust parser
        logger.info("🔄 Retry mode: Searching for FAILED-*.md files...")
        failed_ids = find_failed_files_for_retry(OUTPUT_DIR)

        if not failed_ids:
            logger.info("No failed files found to retry")
            return stats, metrics, state

        # Filter to only those that exist in metadata
        process_indices = [idx for idx in failed_ids if idx in df.index]

        if len(process_indices) < len(failed_ids):
            missing = len(failed_ids) - len(process_indices)
            logger.warning(
                "%d FAILED files not found in current metadata (orphaned)", missing
            )

        logger.info("Found %d failed files to retry", len(process_indices))
        logger.info("(Will delete FAILED-*.md files after successful retry)")
        logger.info("")

    elif indices:
        process_indices = indices
    else:
        process_indices = list(df.index)

    # Filter out already processed if resuming
    if resume and state.processed_files:
        processed_set = set(state.processed_files)
        before_count = len(process_indices)
        process_indices = [idx for idx in process_indices if idx not in processed_set]
        filtered_count = before_count - len(process_indices)
        if filtered_count > 0:
            logger.info("📂 Filtered %d already-processed files", filtered_count)

    # Limit if max_files specified
    if max_files:
        process_indices = process_indices[:max_files]

    stats.total = len(process_indices)
    state.total_files = len(process_indices) + len(state.processed_files)

    if stats.total == 0:
        logger.info("✅ All files already processed!")
        return stats, metrics, state

    logger.info("=" * 70)
    logger.info("Total rows in metadata: %d", len(df))
    logger.info("Files to process: %d", stats.total)
    logger.info("Download workers: %d", download_workers)
    logger.info("Processing workers: %d", processing_workers)
    logger.info("Batch size: %d", batch_size)
    logger.info(
        "System: %d CPUs, %.1fGB RAM",
        os.cpu_count(),
        psutil.virtual_memory().total / (1024**3),
    )
    logger.info("=" * 70)

    # Create aioboto3 session
    s3_config = S3Config.from_env()
    session_kwargs = {}
    if s3_config.region_name:
        session_kwargs["region_name"] = s3_config.region_name

    session = aioboto3.Session(**session_kwargs)

    # Semaphores
    download_semaphore = asyncio.Semaphore(download_workers)

    async def process_with_semaphore(row, idx):
        """Process with download semaphore."""
        if shutdown_requested:
            return
        async with download_semaphore:
            await process_single_pdf(
                session, row, idx, stats, metrics, state, skip_existing, retry_failed
            )

    # Memory sampler
    async def memory_sampler():
        while True:
            await metrics.sample_memory()
            await asyncio.sleep(5)

    memory_task = asyncio.create_task(memory_sampler())
    checkpoint_counter = 0

    try:
        logger.info("")
        logger.info("🔄 Starting processing...")
        logger.info("")

        with tqdm(
            total=stats.total,
            desc="Processing",
            unit="files",
        ) as pbar:
            # Process in batches
            for batch_idx in range(0, len(process_indices), batch_size):
                if shutdown_requested:
                    logger.info("")
                    logger.info("⚠️  Shutdown requested - saving state and exiting")
                    state.save(STATE_FILE)
                    break

                batch = process_indices[batch_idx : batch_idx + batch_size]
                batch_num = (batch_idx // batch_size) + 1
                total_batches = (len(process_indices) + batch_size - 1) // batch_size

                if len(process_indices) > batch_size:
                    logger.info(
                        "Batch %d/%d (%d files)", batch_num, total_batches, len(batch)
                    )

                tasks = []

                async def update_progress(task, pbar):
                    await task
                    async with stats.lock:
                        pbar.set_description(
                            f"Processing [✓{stats.processed} ✗{stats.failed}]"
                        )
                    pbar.update(1)

                for idx in batch:
                    if shutdown_requested:
                        break

                    row = df.loc[idx]
                    task = asyncio.create_task(process_with_semaphore(row, idx))
                    progress_task = asyncio.create_task(update_progress(task, pbar))
                    tasks.append(progress_task)

                # Wait for batch
                if tasks:
                    await asyncio.gather(*tasks, return_exceptions=True)

                # Checkpoint
                checkpoint_counter += len(batch)
                if checkpoint_counter >= checkpoint_interval:
                    state.current_batch = batch_num
                    state.save(STATE_FILE)
                    if len(process_indices) > batch_size:
                        logger.info(
                            "💾 Checkpoint: %d/%d processed",
                            len(state.processed_files),
                            state.total_files,
                        )
                    checkpoint_counter = 0

                # GC between batches
                gc.collect()

                # Memory check
                memory_pct = psutil.virtual_memory().percent
                if memory_pct > MEMORY_THRESHOLD_PERCENT:
                    logger.warning(
                        "⚠️  High memory (%.1f%%), pausing for GC...", memory_pct
                    )
                    gc.collect()
                    await asyncio.sleep(2)

    finally:
        memory_task.cancel()
        state.save(STATE_FILE)

        if not shutdown_requested:
            logger.info("💾 Final checkpoint saved")

    return stats, metrics, state


async def main_async():
    """Main async execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Production-grade async PDF to Markdown processor. "
            "Optimized for processing millions of files with batching, "
            "checkpointing, and graceful shutdown."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Default: Process all new files
  uv run python SimpleWorkflow/pdf_processor.py

  # Retry only failed files
  uv run python SimpleWorkflow/pdf_processor.py --retry-failed

  # Custom workers for large batches
  uv run python SimpleWorkflow/pdf_processor.py \\
      --download-workers 30 --processing-workers 12

  # Process with large batches (millions of files)
  uv run python SimpleWorkflow/pdf_processor.py \\
      --batch-size 1000 --checkpoint-interval 100

  # Resume after interruption
  uv run python SimpleWorkflow/pdf_processor.py --resume

  # Test with sample
  uv run python SimpleWorkflow/pdf_processor.py --sample 100

  # Background processing
  nohup uv run python SimpleWorkflow/pdf_processor.py \\
      --batch-size 1000 > processor.log 2>&1 &
        """,
    )
    parser.add_argument(
        "--max-files", type=int, help="Maximum number of files to process"
    )
    parser.add_argument("--sample", type=int, help="Process a random sample of N files")
    parser.add_argument(
        "--retry-failed",
        action="store_true",
        help="Retry only FAILED-*.md files",
    )
    parser.add_argument(
        "--download-workers",
        type=int,
        default=DEFAULT_DOWNLOAD_WORKERS,
        help=f"Download workers (default: {DEFAULT_DOWNLOAD_WORKERS})",
    )
    parser.add_argument(
        "--processing-workers",
        type=int,
        default=DEFAULT_PROCESSING_WORKERS,
        help=f"Processing workers (default: {DEFAULT_PROCESSING_WORKERS})",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=BATCH_SIZE,
        help=f"Files per batch (default: {BATCH_SIZE}, for millions: 1000)",
    )
    parser.add_argument(
        "--checkpoint-interval",
        type=int,
        default=CHECKPOINT_INTERVAL,
        help=f"Save progress every N files (default: {CHECKPOINT_INTERVAL})",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="Skip existing files (default: True)",
    )
    parser.add_argument(
        "--no-skip-existing",
        dest="skip_existing",
        action="store_false",
        help="Reprocess all files",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        default=True,
        help="Resume from checkpoint (default: True)",
    )
    parser.add_argument(
        "--no-resume",
        dest="resume",
        action="store_false",
        help="Start fresh (ignore checkpoint)",
    )
    parser.add_argument(
        "--clear-state",
        action="store_true",
        help="Clear checkpoint and start fresh",
    )

    args = parser.parse_args()

    # Clear state if requested
    if args.clear_state and STATE_FILE.exists():
        STATE_FILE.unlink()
        logger.info("🗑️  Cleared checkpoint state")

    # Verify environment dependencies
    verify_extraction_dependencies()

    # Ensure directories
    ensure_directories()

    # Load metadata
    logger.info("Loading metadata from %s", METADATA_PATH)
    try:
        df = load_metadata(METADATA_PATH)
        logger.info("✓ Loaded %d rows from metadata", len(df))
    except Exception as e:
        logger.error("Failed to load metadata: %s", e)
        return 1

    # Handle sample mode
    sample_indices = None
    if args.sample:
        logger.info("Sampling %d random files", args.sample)
        sample_indices = df.sample(n=min(args.sample, len(df))).index.tolist()

    # Process files
    stats, metrics, state = await process_batch_async(
        df,
        indices=sample_indices,
        max_files=args.max_files,
        skip_existing=args.skip_existing,
        retry_failed=args.retry_failed,
        download_workers=args.download_workers,
        processing_workers=args.processing_workers,
        batch_size=args.batch_size,
        checkpoint_interval=args.checkpoint_interval,
        resume=args.resume,
    )

    # Log results
    logger.info("")
    stats.log_summary()

    # Performance metrics
    perf = metrics.get_summary()
    logger.info("=" * 70)
    logger.info("PERFORMANCE METRICS")
    logger.info("=" * 70)
    logger.info(
        "  Total time:       %.1fs (%.1f min)",
        perf["total_time"],
        perf["total_time"] / 60,
    )
    logger.info("  Avg download:     %.2fs", perf["avg_download_time"])
    logger.info("  Avg processing:   %.2fs", perf["avg_processing_time"])
    logger.info("  Downloaded:       %.1f MB", perf["total_mb_downloaded"])
    logger.info("  Speed:            %.2f MB/s", perf["download_speed_mbps"])
    logger.info("  Avg memory:       %.0f MB", perf["avg_memory_mb"])
    logger.info("  Peak memory:      %.0f MB", perf["peak_memory_mb"])

    if perf["total_time"] > 0 and stats.processed > 0:
        logger.info(
            "  Throughput:       %.2f files/s", stats.processed / perf["total_time"]
        )

        # Estimate for full dataset
        if stats.total < len(df):
            remaining = len(df) - len(state.processed_files)
            if remaining > 0:
                est_time = remaining / (stats.processed / perf["total_time"])
                logger.info("  Est. remaining:   %.1f hours", est_time / 3600)

    logger.info("=" * 70)

    # Clean state if completed
    if not shutdown_requested and len(state.processed_files) >= state.total_files:
        if STATE_FILE.exists():
            STATE_FILE.unlink()
            logger.info("✓ Processing complete - checkpoint cleared")

    return 0 if stats.failed == 0 else 1


def main():
    """Entry point."""
    return asyncio.run(main_async())


if __name__ == "__main__":
    sys.exit(main())
