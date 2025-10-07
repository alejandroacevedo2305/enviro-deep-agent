"""Retry failed files with high-performance parallelism.

This script analyzes the FAILED-*.md files in ParsedFiles/ and retries parsing
them. It handles common issues that cause PDF parsing failures:

1. PDFs incorrectly marked as compressed files (ZIP) in metadata
2. PDFs with UTF-8 BOM (Byte Order Mark) before the PDF header
3. Empty or corrupted files in S3

The script:
- Scans for all FAILED-*.md files
- Extracts metadata from each failed file
- Downloads PDFs directly from S3 (bypassing ZIP extraction)
- Handles BOM removal automatically
- Shows detailed progress for each file
- Removes FAILED-*.md files after successful parsing
- Reports final statistics

Run it using uv with configurable workers:
    uv run python SimpleWorkflow/retry_failed_files.py \
        --download-workers 15 \
        --processing-workers 4

Or with default auto-detected workers:
    uv run python SimpleWorkflow/retry_failed_files.py

Features:
- High-performance async S3 downloads with configurable parallelism
- Separate semaphores for download vs processing
- Process pool for CPU-bound markdown extraction
- Connection pooling optimization
- Performance metrics tracking
- Memory-aware task scheduling
- Detailed progress tracking with success/failure counts
- Automatic cleanup of successful retries
- Handles UTF-8 BOM automatically
"""

# %%
from __future__ import annotations

import asyncio
import gc
import logging
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import aioboto3
import pandas as pd
import psutil
from dotenv import load_dotenv
from tqdm.asyncio import tqdm

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from localPDFparse.parse import extract_markdown
from s3pdf_manager.download_pdf import (
    S3Config,
    _resolve_bucket_and_key,
    _sanitize_filename_component,
    load_metadata,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("SimpleWorkflow/retry_processing.log", mode="a"),
    ],
)
logger = logging.getLogger(__name__)

# Suppress verbose boto3 logging
logging.getLogger("boto3").setLevel(logging.WARNING)
logging.getLogger("botocore").setLevel(logging.WARNING)
logging.getLogger("aiobotocore").setLevel(logging.WARNING)

# Load environment variables
load_dotenv()

# Constants
OUTPUT_DIR = Path("SimpleWorkflow/ParsedFiles")
PARQUET_PATH = "sql/metadata_table/flora_fauna_metadata_indexed.parquet"
MAX_RETRIES = 3
RETRY_DELAY = 1


# Auto-detect optimal workers based on system resources
def get_optimal_workers() -> tuple[int, int]:
    """Calculate optimal number of download and processing workers."""
    cpu_count = os.cpu_count() or 4
    memory_gb = psutil.virtual_memory().total / (1024**3)

    # Download workers: I/O bound, can be higher
    # Rule: 2-3x CPU cores, capped by memory
    download_workers = min(cpu_count * 3, int(memory_gb * 2), 20)

    # Processing workers: CPU and memory intensive
    # Rule: CPU cores - 1, capped by memory
    processing_workers = min(max(cpu_count - 1, 2), int(memory_gb / 2), 10)

    return download_workers, processing_workers


DEFAULT_DOWNLOAD_WORKERS, DEFAULT_PROCESSING_WORKERS = get_optimal_workers()


@dataclass
class PerformanceMetrics:
    """Track detailed performance metrics."""

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
class RetryStats:
    """Track retry statistics."""

    total: int = 0
    success: int = 0
    failed: int = 0
    errors: list[tuple[str, str]] = field(default_factory=list)
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def increment_success(self):
        async with self.lock:
            self.success += 1

    async def increment_failed(self, file_id: str, error: str):
        async with self.lock:
            self.failed += 1
            self.errors.append((file_id, error))

    def log_summary(self):
        """Log retry summary."""
        logger.info("=" * 70)
        logger.info("RETRY PROCESS COMPLETED")
        logger.info("=" * 70)
        logger.info("")
        logger.info("📈 Final Results:")
        logger.info("   ✓ Successful: %d/%d", self.success, self.total)
        logger.info("   ✗ Failed:     %d/%d", self.failed, self.total)
        success_rate = (self.success / self.total * 100) if self.total > 0 else 0
        logger.info("   Success Rate: %.1f%%", success_rate)
        logger.info("")


def parse_failed_file_metadata(failed_file_path: Path) -> Optional[dict]:
    """Parse metadata from a FAILED-*.md file.

    Returns:
        Dictionary with file_identifier, s3_key, and error info, or None.
    """
    try:
        content = failed_file_path.read_text(encoding="utf-8")
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


def find_failed_files() -> list[tuple[Path, dict]]:
    """Find all FAILED-*.md files and parse their metadata.

    Returns:
        List of tuples (file_path, metadata_dict).
    """
    failed_files = []

    for failed_path in OUTPUT_DIR.glob("FAILED-*.md"):
        metadata = parse_failed_file_metadata(failed_path)
        if metadata:
            failed_files.append((failed_path, metadata))
            logger.info(
                "Found failed file: %s (error: %s)",
                metadata["file_identifier"],
                metadata.get("error", "unknown"),
            )
        else:
            logger.warning("Could not parse metadata from %s", failed_path)

    return failed_files


async def download_from_s3_async(
    session: aioboto3.Session,
    bucket: str,
    s3_key: str,
    metrics: PerformanceMetrics,
    max_retries: int = MAX_RETRIES,
) -> bytes:
    """Download file from S3 asynchronously with retries and metrics.

    Args:
        session: aioboto3 session
        bucket: S3 bucket name
        s3_key: S3 object key
        metrics: Performance metrics tracker
        max_retries: Maximum number of retry attempts

    Returns:
        File content as bytes
    """
    start_time = time.time()

    for attempt in range(max_retries):
        try:
            async with session.client("s3") as s3_client:
                response = await s3_client.get_object(Bucket=bucket, Key=s3_key)
                content = await response["Body"].read()

                duration = time.time() - start_time
                await metrics.add_download_time(duration, len(content))
                return content

        except Exception:
            if attempt < max_retries - 1:
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))
            else:
                raise


def extract_markdown_worker(pdf_path_str: str) -> tuple[str, any]:
    """Worker function for PDF extraction (must be picklable).

    Args:
        pdf_path_str: Path to PDF file as string

    Returns:
        Tuple of (markdown_content, error_or_None)
    """
    try:
        # extract_markdown returns (markdown_text, metadata)
        markdown_text, _metadata = extract_markdown(pdf_path_str)
        return markdown_text, None
    except Exception as exc:
        logger.error("Markdown extraction failed for %s: %s", pdf_path_str, exc)
        return "", exc


async def process_pdf_async(
    pdf_bytes: bytes,
    file_identifier: str,
    executor: ProcessPoolExecutor,
    metrics: PerformanceMetrics,
) -> tuple[bool, str, Optional[str]]:
    """Process PDF bytes to markdown asynchronously.

    Args:
        pdf_bytes: PDF content as bytes
        file_identifier: Unique identifier for the file
        executor: ProcessPoolExecutor for CPU-bound markdown extraction
        metrics: Performance metrics tracker

    Returns:
        Tuple of (success, markdown_content, error_message)
    """
    start_time = time.time()
    temp_dir = Path("SimpleWorkflow/.temp")
    temp_dir.mkdir(parents=True, exist_ok=True)

    safe_name = _sanitize_filename_component(file_identifier)
    temp_pdf_path = temp_dir / f"{safe_name}.pdf"

    try:
        # Write PDF to temp file
        temp_pdf_path.write_bytes(pdf_bytes)

        # Extract markdown using process pool
        loop = asyncio.get_event_loop()
        markdown, error = await loop.run_in_executor(
            executor, extract_markdown_worker, str(temp_pdf_path)
        )

        if error:
            return False, "", str(error)

        duration = time.time() - start_time
        await metrics.add_processing_time(duration)

        return True, markdown, None

    except Exception as exc:
        logger.error("PDF processing failed for %s: %s", file_identifier, exc)
        return False, "", str(exc)
    finally:
        # Clean up temp file
        if temp_pdf_path.exists():
            try:
                temp_pdf_path.unlink()
            except Exception as cleanup_exc:
                logger.warning(
                    "Failed to delete temp file %s: %s",
                    temp_pdf_path,
                    cleanup_exc,
                )


async def retry_single_file(
    session: aioboto3.Session,
    failed_path: Path,
    metadata: dict,
    df_metadata: pd.DataFrame,
    executor: ProcessPoolExecutor,
    stats: RetryStats,
    metrics: PerformanceMetrics,
) -> bool:
    """Retry processing a single failed file with optimized async handling.

    Args:
        session: aioboto3 session
        failed_path: Path to the FAILED-*.md file
        metadata: Parsed metadata from the failed file
        df_metadata: Full metadata DataFrame
        executor: ProcessPoolExecutor for markdown extraction
        stats: Retry statistics tracker
        metrics: Performance metrics tracker

    Returns:
        True if successful, False otherwise
    """
    file_identifier = metadata["file_identifier"]
    s3_key = metadata["s3_key"]

    try:
        # Try to get additional info from metadata DataFrame
        row = None
        if file_identifier in df_metadata.index:
            row = df_metadata.loc[file_identifier]
            bucket, s3_key = _resolve_bucket_and_key(row)
        else:
            # Extract bucket from s3_key if it's in s3:// format
            if s3_key.startswith("s3://"):
                parts = s3_key[5:].split("/", 1)
                bucket = parts[0]
                s3_key = parts[1]
            else:
                # Parse from sea-crawler pattern
                bucket = "sea-crawler"
                # s3_key is already in the correct format

        # Download from S3 (treating as direct PDF, not ZIP)
        pdf_bytes = await download_from_s3_async(session, bucket, s3_key, metrics)

        # Check for empty files
        if len(pdf_bytes) == 0:
            raise ValueError("Empty file (0 bytes)")

        # Remove UTF-8 BOM if present (some files have this)
        if pdf_bytes.startswith(b"\xef\xbb\xbf"):
            pdf_bytes = pdf_bytes[3:]

        # Verify it's actually a PDF
        if not pdf_bytes.startswith(b"%PDF"):
            raise ValueError(f"Not a PDF file (starts with: {pdf_bytes[:20]!r})")

        # Process PDF to markdown
        success, markdown_content, error_msg = await process_pdf_async(
            pdf_bytes, file_identifier, executor, metrics
        )

        if not success:
            raise RuntimeError(f"Markdown extraction failed: {error_msg}")

        # Save successful result
        output_path = OUTPUT_DIR / f"{file_identifier}.md"
        output_path.write_text(markdown_content, encoding="utf-8")

        # Remove the FAILED file
        failed_path.unlink()

        await stats.increment_success()
        return True

    except Exception as exc:
        error_msg = f"{type(exc).__name__}: {exc}"
        await stats.increment_failed(file_identifier, error_msg)
        logger.debug("Full error for %s:", file_identifier, exc_info=True)
        return False


async def retry_all_failed_files(
    download_workers: int = DEFAULT_DOWNLOAD_WORKERS,
    processing_workers: int = DEFAULT_PROCESSING_WORKERS,
):
    """Main async function to retry all failed files with parallelism.

    Args:
        download_workers: Number of concurrent download workers
        processing_workers: Number of concurrent processing workers
    """
    # Initialize stats and metrics
    stats = RetryStats()
    metrics = PerformanceMetrics()

    # Find all failed files
    logger.info("=" * 70)
    logger.info("FAILED FILES RETRY PROCESS")
    logger.info("=" * 70)
    logger.info("")

    failed_files = find_failed_files()

    if not failed_files:
        logger.info("No failed files found to retry.")
        return stats, metrics

    stats.total = len(failed_files)
    logger.info("📊 Found %d failed files to retry", stats.total)

    # Load metadata
    try:
        logger.info("📖 Loading metadata...")
        df_metadata = load_metadata(PARQUET_PATH)
        logger.info("✓ Loaded metadata with %d rows", len(df_metadata))
    except Exception as exc:
        logger.error("✗ Failed to load metadata: %s", exc)
        return stats, metrics

    # System info
    logger.info("=" * 70)
    logger.info("Download workers: %d", download_workers)
    logger.info("Processing workers: %d", processing_workers)
    logger.info(
        "System: %d CPUs, %.1fGB RAM",
        os.cpu_count(),
        psutil.virtual_memory().total / (1024**3),
    )
    logger.info("=" * 70)

    # Create async S3 session with connection pooling
    s3_config = S3Config.from_env()
    session_kwargs = {}
    if s3_config.region_name:
        session_kwargs["region_name"] = s3_config.region_name

    session = aioboto3.Session(**session_kwargs)

    # Create process pool for CPU-bound markdown extraction
    executor = ProcessPoolExecutor(max_workers=processing_workers)

    # Separate semaphores for downloads and processing
    download_semaphore = asyncio.Semaphore(download_workers)

    async def retry_with_semaphore(failed_path: Path, metadata: dict):
        """Retry with download semaphore."""
        async with download_semaphore:
            await retry_single_file(
                session,
                failed_path,
                metadata,
                df_metadata,
                executor,
                stats,
                metrics,
            )

    # Sample memory periodically
    async def memory_sampler():
        while True:
            await metrics.sample_memory()
            await asyncio.sleep(5)

    memory_task = asyncio.create_task(memory_sampler())

    try:
        logger.info("")
        logger.info("🔄 Starting retry process...")
        logger.info("")

        # Process with progress bar
        with tqdm(
            total=stats.total,
            desc="Retrying",
            unit="files",
            bar_format=(
                "{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} "
                "[{elapsed}<{remaining}, {rate_fmt}]"
            ),
        ) as pbar:
            tasks = []
            for failed_path, metadata in failed_files:
                task = asyncio.create_task(retry_with_semaphore(failed_path, metadata))

                # Update progress on completion
                task.add_done_callback(lambda _: pbar.update(1))
                tasks.append(task)

                # Batch task creation to avoid memory spike
                if len(tasks) >= download_workers * 2:
                    await asyncio.gather(*tasks, return_exceptions=True)
                    tasks = []
                    gc.collect()  # Periodic GC

            # Wait for remaining tasks
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)

    finally:
        memory_task.cancel()
        executor.shutdown(wait=True)

    return stats, metrics


async def main_async():
    """Main async execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description="High-performance retry for failed PDF parsing"
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

    args = parser.parse_args()

    # Run retry process
    stats, metrics = await retry_all_failed_files(
        download_workers=args.download_workers,
        processing_workers=args.processing_workers,
    )

    # Log results
    stats.log_summary()

    perf = metrics.get_summary()
    logger.info("=" * 70)
    logger.info("Performance Metrics:")
    logger.info("  Total time: %.1fs", perf["total_time"])
    logger.info("  Avg download: %.2fs", perf["avg_download_time"])
    logger.info("  Avg processing: %.2fs", perf["avg_processing_time"])
    logger.info("  Downloaded: %.1f MB", perf["total_mb_downloaded"])
    logger.info("  Speed: %.2f MB/s", perf["download_speed_mbps"])
    logger.info("  Avg memory: %.0f MB", perf["avg_memory_mb"])
    logger.info("  Peak memory: %.0f MB", perf["peak_memory_mb"])
    if perf["total_time"] > 0 and stats.success > 0:
        logger.info(
            "  Throughput: %.2f files/s",
            stats.success / perf["total_time"],
        )
    logger.info("=" * 70)

    return 0 if stats.failed == 0 else 1


def main():
    """Entry point."""
    return asyncio.run(main_async())


if __name__ == "__main__":
    sys.exit(main())
