"""Robust PDF to Markdown converter with timeout and signal handling.

This enhanced version includes:
- Signal handling for graceful shutdown on Linux
- Per-file timeout mechanism to prevent hanging
- Progress state saving for resume capability
- Memory monitoring and garbage collection
- Better error recovery and reporting

Run it using uv:
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py
"""

# %%
from __future__ import annotations

import gc
import json
import logging
import os
import signal
import sys
import tempfile
import time
import traceback
from concurrent.futures import ProcessPoolExecutor, TimeoutError
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import pandas as pd
import psutil
from dotenv import load_dotenv
from tqdm import tqdm

# Import modules from the project
sys.path.insert(0, str(Path(__file__).parent.parent))
from localPDFparse.parse import extract_markdown
from s3pdf_manager.download_pdf import (
    S3Config,
    S3Downloader,
    _looks_like_pdf,
    _resolve_bucket_and_key,
    _sanitize_filename_component,
)

# Load environment variables
load_dotenv()

# Configure logging with more detailed format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s | PID:%(process)d",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("SimpleWorkflow/processing_robust.log", mode="a"),
    ],
)
logger = logging.getLogger(__name__)

# Constants
METADATA_PATH = "sql/metadata_table/flora_fauna_metadata_indexed.parquet"
OUTPUT_DIR = Path("SimpleWorkflow/ParsedFiles")
TEMP_DIR = Path(tempfile.gettempdir()) / "pdf_processing"
STATE_FILE = Path("SimpleWorkflow/.processing_state.json")
MAX_RETRIES = 3
RETRY_DELAY = 2
FILE_TIMEOUT = 300  # 5 minutes timeout per file
DOWNLOAD_TIMEOUT = 120  # 2 minutes timeout for download
MEMORY_THRESHOLD_MB = 4000  # Trigger GC if memory usage exceeds this

# Global flag for graceful shutdown
shutdown_requested = False


def signal_handler(signum, frame):
    """Handle shutdown signals gracefully."""
    global shutdown_requested
    logger.warning(f"Received signal {signum}. Initiating graceful shutdown...")
    shutdown_requested = True


# Register signal handlers for Linux
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGHUP, signal.SIG_IGN)  # Ignore hangup signal


@dataclass
class ProcessingState:
    """Track processing state for resume capability."""

    start_time: str = ""
    last_update: str = ""
    total_files: int = 0
    processed_files: list[str] = field(default_factory=list)
    failed_files: list[str] = field(default_factory=list)
    skipped_files: list[str] = field(default_factory=list)
    current_file: Optional[str] = None
    memory_usage_mb: float = 0
    pid: int = os.getpid()

    def save(self):
        """Save state to file."""
        self.last_update = datetime.now().isoformat()
        self.memory_usage_mb = get_memory_usage()

        state_dict = {
            "start_time": self.start_time,
            "last_update": self.last_update,
            "total_files": self.total_files,
            "processed_files": self.processed_files,
            "failed_files": self.failed_files,
            "skipped_files": self.skipped_files,
            "current_file": self.current_file,
            "memory_usage_mb": self.memory_usage_mb,
            "pid": self.pid,
        }

        try:
            STATE_FILE.write_text(json.dumps(state_dict, indent=2))
            logger.debug(f"State saved: {len(self.processed_files)} processed")
        except Exception as e:
            logger.error(f"Failed to save state: {e}")

    @classmethod
    def load(cls) -> Optional[ProcessingState]:
        """Load state from file if exists."""
        if not STATE_FILE.exists():
            return None

        try:
            state_dict = json.loads(STATE_FILE.read_text())
            state = cls()
            for key, value in state_dict.items():
                if hasattr(state, key):
                    setattr(state, key, value)
            return state
        except Exception as e:
            logger.error(f"Failed to load state: {e}")
            return None

    def clear(self):
        """Clear the state file."""
        if STATE_FILE.exists():
            STATE_FILE.unlink()
            logger.info("Processing state cleared")


def get_memory_usage() -> float:
    """Get current memory usage in MB."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024


def check_memory_and_gc():
    """Check memory usage and trigger garbage collection if needed."""
    memory_mb = get_memory_usage()
    if memory_mb > MEMORY_THRESHOLD_MB:
        logger.warning(
            f"High memory usage: {memory_mb:.1f} MB. Triggering garbage collection..."
        )
        gc.collect()
        new_memory_mb = get_memory_usage()
        logger.info(
            f"Memory after GC: {new_memory_mb:.1f} MB "
            f"(freed {memory_mb - new_memory_mb:.1f} MB)"
        )


def _extract_pdf_from_zip_bytes(
    zip_bytes: bytes, prefer_name: Optional[str] = None
) -> tuple[str, bytes]:
    """Extract a PDF file from ZIP archive bytes."""
    import zipfile
    from io import BytesIO

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
            logger.info(f"Multiple PDFs found, selecting largest: {selected_pdf}")

        pdf_bytes = zf.read(selected_pdf)
        return selected_pdf, pdf_bytes


def _extract_markdown_worker(pdf_path_str: str) -> tuple[str, Any]:
    """Worker function for PDF extraction (must be picklable)."""
    return extract_markdown(
        Path(pdf_path_str),
        output_dir=None,
        ignore_images=True,
        clean_text=True,
        validate_quality=True,
        show_progress=False,
    )


def process_pdf_with_timeout(
    pdf_path: Path, index_value: str, timeout: Optional[int] = None
) -> tuple[str, Any]:
    """Process PDF with timeout using process pool."""

    if timeout is None:
        timeout = FILE_TIMEOUT

    # Use ProcessPoolExecutor for true process isolation
    with ProcessPoolExecutor(max_workers=1) as executor:
        future = executor.submit(_extract_markdown_worker, str(pdf_path))
        try:
            result = future.result(timeout=timeout)
            return result
        except TimeoutError:
            logger.error(f"Timeout processing {index_value} after {timeout}s")
            # Force kill the process if it's still running
            executor.shutdown(wait=False, cancel_futures=True)
            raise TimeoutError(f"PDF processing exceeded {timeout}s timeout")
        except Exception as e:
            logger.error(f"Error in subprocess for {index_value}: {e}")
            raise


def download_with_timeout(
    downloader: S3Downloader,
    bucket: str,
    key: str,
    output_path: Optional[Path] = None,
    timeout: Optional[int] = None,
) -> bytes:
    """Download from S3 with timeout."""
    import threading

    if timeout is None:
        timeout = DOWNLOAD_TIMEOUT

    result = {"data": None, "error": None}

    def _download():
        try:
            if output_path:
                downloader.download_to_file(bucket, key, output_path)
                result["data"] = output_path.read_bytes()
            else:
                result["data"] = downloader.download_to_memory(bucket, key)
        except Exception as e:
            result["error"] = e

    thread = threading.Thread(target=_download)
    thread.daemon = True
    thread.start()
    thread.join(timeout=timeout)

    if thread.is_alive():
        logger.error(f"Download timeout for s3://{bucket}/{key} after {timeout}s")
        raise TimeoutError(f"Download exceeded {timeout}s timeout")

    if result["error"]:
        raise result["error"]

    return result["data"]


def save_error_markdown(
    index_value: str,
    error: Exception,
    row: pd.Series,
    s3_key: str = None,
    retry_count: int = 0,
) -> None:
    """Save error details to a markdown file for debugging."""
    safe_index = _sanitize_filename_component(index_value)
    error_path = OUTPUT_DIR / f"FAILED-{safe_index}.md"

    error_content = f"""---
file_identifier: {index_value}
status: FAILED
error_type: {type(error).__name__}
error_time: {pd.Timestamp.now().isoformat()}
retry_attempts: {retry_count}
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
- **AWS URL:** {row.get("aws_url", "N/A")}

## Row Data
```json
{row.to_json(indent=2) if hasattr(row, "to_json") else str(row)}
```

## Next Steps

1. Check if the S3 key is valid and accessible
2. Verify the file type matches the metadata (PDF vs ZIP)
3. Check AWS credentials and permissions
4. Review the error message and traceback above
5. If timeout error, consider increasing FILE_TIMEOUT
6. If memory error, process in smaller batches

---
*This error report was automatically generated*
"""

    try:
        error_path.write_text(error_content, encoding="utf-8")
        logger.info(f"Saved error report: {error_path}")
    except Exception as e:
        logger.error(f"Failed to save error report for {index_value}: {e}")


def process_single_pdf_robust(
    row: pd.Series,
    index_value: str,
    downloader: S3Downloader,
    state: ProcessingState,
    skip_existing: bool = True,
) -> tuple[bool, str]:
    """Process a single PDF with robust error handling and timeout."""
    global shutdown_requested

    if shutdown_requested:
        logger.info("Shutdown requested, skipping processing")
        return False, "skipped"

    # Update state
    state.current_file = index_value
    state.save()

    # Check memory before processing
    check_memory_and_gc()

    safe_index = _sanitize_filename_component(index_value)
    markdown_path = OUTPUT_DIR / f"{safe_index}.md"
    error_path = OUTPUT_DIR / f"FAILED-{safe_index}.md"

    # Skip if already processed
    if skip_existing and markdown_path.exists():
        logger.debug(f"Skipping existing: {markdown_path}")
        state.skipped_files.append(index_value)
        return True, "skipped"

    if skip_existing and error_path.exists():
        logger.debug(f"Skipping previously failed: {error_path}")
        state.skipped_files.append(index_value)
        return True, "skipped"

    temp_pdf_path = TEMP_DIR / f"{safe_index}.pdf"
    s3_key = None

    try:
        # Resolve S3 bucket and key
        bucket, s3_key = _resolve_bucket_and_key(row)

        # Skip macOS system files
        if "__MACOSX" in s3_key or "/._" in s3_key or s3_key.startswith("._"):
            logger.info(f"Skipping macOS system file: {s3_key}")
            state.skipped_files.append(index_value)
            return True, "skipped"

        from_zip = bool(row.get("from_compressed_file", False))

        logger.info(f"Downloading from s3://{bucket}/{s3_key}")

        # Download with timeout and retries
        content = None
        for attempt in range(MAX_RETRIES):
            if shutdown_requested:
                logger.info("Shutdown requested during download")
                return False, "interrupted"

            try:
                if from_zip:
                    content = download_with_timeout(
                        downloader, bucket, s3_key, timeout=DOWNLOAD_TIMEOUT
                    )

                    if _looks_like_pdf(content):
                        logger.info("File marked as compressed but is actually a PDF")
                        temp_pdf_path.write_bytes(content)
                    else:
                        prefer_name = row.get("file_name")
                        internal_name, pdf_bytes = _extract_pdf_from_zip_bytes(
                            content, prefer_name=prefer_name
                        )
                        logger.info(f"Extracted '{internal_name}' from ZIP")
                        temp_pdf_path.write_bytes(pdf_bytes)
                else:
                    download_with_timeout(
                        downloader,
                        bucket,
                        s3_key,
                        temp_pdf_path,
                        timeout=DOWNLOAD_TIMEOUT,
                    )
                break
            except TimeoutError:
                if attempt < MAX_RETRIES - 1:
                    logger.warning(
                        f"Download timeout, attempt {attempt + 1}/{MAX_RETRIES}"
                    )
                    time.sleep(RETRY_DELAY * (attempt + 1))
                else:
                    raise
            except Exception as e:
                if attempt < MAX_RETRIES - 1:
                    logger.warning(
                        f"Download failed, attempt {attempt + 1}/{MAX_RETRIES}: {e}"
                    )
                    time.sleep(RETRY_DELAY)
                    if temp_pdf_path.exists():
                        temp_pdf_path.unlink()
                else:
                    raise

        if not temp_pdf_path.exists():
            raise FileNotFoundError(
                f"PDF file not found after download: {temp_pdf_path}"
            )

        file_size_mb = temp_pdf_path.stat().st_size / (1024 * 1024)
        logger.info(f"PDF file size: {file_size_mb:.2f} MB")

        # Adjust timeout based on file size
        adjusted_timeout = FILE_TIMEOUT
        if file_size_mb > 50:
            adjusted_timeout = int(FILE_TIMEOUT * (1 + file_size_mb / 100))
            logger.info(f"Large file, adjusted timeout to {adjusted_timeout}s")

        # Process PDF with timeout
        logger.info(f"Converting to markdown (timeout: {adjusted_timeout}s)")
        markdown_content, metadata = process_pdf_with_timeout(
            temp_pdf_path, index_value, timeout=adjusted_timeout
        )

        # Add metadata header
        header = f"""---
file_identifier: {index_value}
s3_key: {s3_key}
nombre: {row.get("nombre", "N/A")}
fecha_presentacion: {row.get("fecha_de_presentacion", "N/A")}
region: {row.get("region", "N/A")}
tipo_proyecto: {row.get("tipo_de_proyecto", "N/A")}
extraction_quality: {metadata.extraction_quality.value}
page_count: {metadata.page_count}
processing_time: {datetime.now().isoformat()}
---

"""
        full_markdown = header + markdown_content

        # Clean Unicode
        full_markdown = full_markdown.encode("utf-8", errors="ignore").decode(
            "utf-8", errors="ignore"
        )

        # Save markdown
        markdown_path.write_text(full_markdown, encoding="utf-8")
        logger.info(f"✓ Saved: {markdown_path}")

        # Update state
        state.processed_files.append(index_value)
        state.save()

        # Clean up any previous error report
        if error_path.exists():
            error_path.unlink()

        return True, "processed"

    except Exception as e:
        logger.error(f"Failed to process {index_value}: {str(e)}")
        save_error_markdown(index_value, e, row, s3_key)

        # Update state
        state.failed_files.append(index_value)
        state.save()

        return False, "failed"

    finally:
        # Clean up temp file
        if temp_pdf_path.exists():
            temp_pdf_path.unlink()

        # Clear current file in state
        state.current_file = None
        state.save()


def ensure_directories():
    """Ensure required directories exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory: {OUTPUT_DIR}")
    logger.info(f"Temp directory: {TEMP_DIR}")


def process_batch_robust(
    df: pd.DataFrame,
    indices: Optional[list[str]] = None,
    max_files: Optional[int] = None,
    skip_existing: bool = True,
    resume: bool = False,
) -> int:
    """Process a batch of PDFs with robust error handling."""
    global shutdown_requested

    # Load or create state
    state = ProcessingState.load() if resume else ProcessingState()
    if not state.start_time:
        state.start_time = datetime.now().isoformat()

    # Determine indices to process
    if indices:
        process_indices = indices
    else:
        process_indices = list(df.index)

    # Resume from where we left off
    if resume and state.processed_files:
        logger.info(
            f"Resuming from previous state: {len(state.processed_files)} already processed"
        )
        process_indices = [
            idx
            for idx in process_indices
            if idx not in state.processed_files and idx not in state.failed_files
        ]

    if max_files:
        process_indices = process_indices[:max_files]

    state.total_files = len(process_indices)

    logger.info("=" * 60)
    logger.info(f"Total rows in metadata: {len(df):,}")
    logger.info(f"Files to process: {state.total_files:,}")
    logger.info(f"Memory usage: {get_memory_usage():.1f} MB")
    logger.info(f"Process PID: {os.getpid()}")
    logger.info("=" * 60)

    # Initialize S3 downloader
    config = S3Config.from_env()
    downloader = S3Downloader(config)

    # Statistics
    processed = 0
    skipped = 0
    failed = 0

    # Process with progress bar
    with tqdm(
        total=state.total_files,
        desc="Processing",
        unit="files",
        bar_format=(
            "{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} "
            "[{elapsed}<{remaining}, {rate_fmt}]"
        ),
    ) as pbar:
        for idx in process_indices:
            if shutdown_requested:
                logger.warning("Graceful shutdown initiated")
                break

            try:
                row = df.loc[idx]
                success, status = process_single_pdf_robust(
                    row, idx, downloader, state, skip_existing=skip_existing
                )

                if status == "skipped":
                    skipped += 1
                elif status == "processed":
                    processed += 1
                elif status == "failed":
                    failed += 1
                elif status == "interrupted":
                    break

                # Update progress bar
                pbar.update(1)
                pbar.set_postfix_str(
                    f"✓{processed} ⏭{skipped} ✗{failed} 💾{get_memory_usage():.0f}MB"
                )

            except Exception as e:
                failed += 1
                logger.error(f"Unexpected error processing {idx}: {e}")
                state.failed_files.append(idx)
                state.save()
                pbar.update(1)
                pbar.set_postfix_str(
                    f"✓{processed} ⏭{skipped} ✗{failed} 💾{get_memory_usage():.0f}MB"
                )

    # Final summary
    logger.info("-" * 60)
    logger.info("Processing Summary:")
    logger.info(f"  Total files: {state.total_files}")
    logger.info(f"  Processed: {processed}")
    logger.info(f"  Skipped: {skipped}")
    logger.info(f"  Failed: {failed}")
    logger.info(f"  Memory usage: {get_memory_usage():.1f} MB")

    if shutdown_requested:
        logger.warning("Processing interrupted by shutdown signal")
        logger.info("State saved. Use --resume to continue from where you left off")
    else:
        logger.info("Processing completed successfully")
        state.clear()

    return 0 if failed == 0 else 1


def main():
    """Main execution function."""
    global FILE_TIMEOUT, MEMORY_THRESHOLD_MB
    import argparse

    parser = argparse.ArgumentParser(
        description="Robust PDF to Markdown converter with timeout and signal handling"
    )
    parser.add_argument(
        "--indices",
        nargs="+",
        help="Specific file identifiers to process",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        help="Maximum number of files to process",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="Skip files that already have markdown (default: True)",
    )
    parser.add_argument(
        "--no-skip-existing",
        dest="skip_existing",
        action="store_false",
        help="Reprocess all files even if markdown exists",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from previous processing state",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=FILE_TIMEOUT,
        help=f"Timeout in seconds per file (default: {FILE_TIMEOUT})",
    )
    parser.add_argument(
        "--memory-limit",
        type=int,
        default=MEMORY_THRESHOLD_MB,
        help=f"Memory limit in MB before GC (default: {MEMORY_THRESHOLD_MB})",
    )

    args = parser.parse_args()

    # Update global settings
    FILE_TIMEOUT = args.timeout
    MEMORY_THRESHOLD_MB = args.memory_limit

    logger.info(f"Starting robust PDF processor (PID: {os.getpid()})")
    logger.info(f"Timeout per file: {FILE_TIMEOUT}s")
    logger.info(f"Memory threshold: {MEMORY_THRESHOLD_MB} MB")

    # Ensure directories exist
    ensure_directories()

    # Load metadata
    logger.info(f"Loading metadata from {METADATA_PATH}")
    try:
        df = pd.read_parquet(METADATA_PATH)
        logger.info(f"✓ Loaded {len(df):,} rows from metadata")
    except Exception as e:
        logger.error(f"Failed to load metadata: {e}")
        return 1

    # Process files
    return process_batch_robust(
        df,
        indices=args.indices,
        max_files=args.max_files,
        skip_existing=args.skip_existing,
        resume=args.resume,
    )


if __name__ == "__main__":
    sys.exit(main())
