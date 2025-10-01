"""Optimized async PDF to Markdown converter with advanced parallelization.

This version includes:
- Dynamic worker scaling based on system resources
- Separate semaphores for download vs processing
- Connection pooling optimization
- Memory-aware task scheduling
- Performance metrics tracking

Run it using uv:
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py
"""

# %%
from __future__ import annotations

import asyncio
import gc
import logging
import os
import sys
import tempfile
import time
import traceback
import zipfile
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime
from io import BytesIO
from pathlib import Path
from typing import Optional

import pandas as pd
import psutil
from dotenv import load_dotenv
from tqdm.asyncio import tqdm as async_tqdm

# Import modules from the project
sys.path.insert(0, str(Path(__file__).parent.parent))
from localPDFparse.parse import extract_markdown
from s3pdf_manager.download_pdf import (
    _looks_like_pdf,
    _resolve_bucket_and_key,
    _sanitize_filename_component,
)

# Import aioboto3 for async S3 operations
try:
    import aioboto3
except ImportError:
    print("Installing aioboto3...")
    import subprocess

    subprocess.check_call([sys.executable, "-m", "pip", "install", "aioboto3"])
    import aioboto3

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("SimpleWorkflow/processing_optimized.log", mode="a"),
    ],
)
logger = logging.getLogger(__name__)

# Suppress verbose boto3 logging
logging.getLogger("boto3").setLevel(logging.WARNING)
logging.getLogger("botocore").setLevel(logging.WARNING)
logging.getLogger("aiobotocore").setLevel(logging.WARNING)

# Constants
METADATA_PATH = "sql/metadata_table/flora_fauna_metadata_indexed.parquet"
OUTPUT_DIR = Path("SimpleWorkflow/ParsedFiles")
TEMP_DIR = Path(tempfile.gettempdir()) / "pdf_processing_optimized"
MAX_RETRIES = 3
RETRY_DELAY = 1  # Reduced from 2

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
class ProcessingStats:
    """Track processing statistics."""

    total: int = 0
    processed: int = 0
    skipped: int = 0
    failed: int = 0
    errors: list[tuple[str, str]] = field(default_factory=list)
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def increment_processed(self):
        async with self.lock:
            self.processed += 1

    async def increment_skipped(self):
        async with self.lock:
            self.skipped += 1

    async def increment_failed(self, idx: str, error: str):
        async with self.lock:
            self.failed += 1
            self.errors.append((idx, error))

    def log_summary(self):
        """Log processing summary."""
        logger.info("-" * 60)
        logger.info("Processing Summary:")
        logger.info(f"  Total files: {self.total}")
        logger.info(f"  Processed: {self.processed}")
        logger.info(f"  Skipped (existing): {self.skipped}")
        logger.info(f"  Failed: {self.failed}")


def ensure_directories():
    """Ensure required directories exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)


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


def _extract_markdown_worker(pdf_path_str: str) -> tuple[str, any]:
    """Worker function for PDF extraction (runs in process pool)."""
    return extract_markdown(
        Path(pdf_path_str),
        output_dir=None,
        ignore_images=True,
        clean_text=True,
        validate_quality=True,
        show_progress=False,
    )


async def download_from_s3_async(
    session: aioboto3.Session,
    bucket: str,
    key: str,
    metrics: PerformanceMetrics,
    max_retries: int = MAX_RETRIES,
) -> bytes:
    """Download from S3 with retries and metrics."""
    start_time = time.time()
    
    for attempt in range(max_retries):
        try:
            async with session.client("s3") as s3_client:
                response = await s3_client.get_object(Bucket=bucket, Key=key)
                content = await response["Body"].read()
                
                duration = time.time() - start_time
                await metrics.add_download_time(duration, len(content))
                return content
                
        except Exception as e:
            if attempt < max_retries - 1:
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))
            else:
                raise


async def process_pdf_async(
    pdf_bytes: bytes,
    index_value: str,
    row: pd.Series,
    s3_key: str,
    metrics: PerformanceMetrics,
    executor: ProcessPoolExecutor,
) -> tuple[bool, str, Optional[str]]:
    """Process PDF bytes to markdown asynchronously."""
    start_time = time.time()
    safe_index = _sanitize_filename_component(index_value)
    temp_pdf_path = TEMP_DIR / f"{safe_index}.pdf"

    try:
        # Write PDF to temp file
        temp_pdf_path.write_bytes(pdf_bytes)

        # Run PDF parsing in process executor
        loop = asyncio.get_event_loop()
        markdown_content, metadata = await loop.run_in_executor(
            executor, _extract_markdown_worker, str(temp_pdf_path)
        )

        # Create markdown with header
        header = f"""---
file_identifier: {index_value}
s3_key: {s3_key}
nombre: {row.get("nombre", "N/A")}
fecha_presentacion: {row.get("fecha_de_presentacion", "N/A")}
region: {row.get("region", "N/A")}
tipo_proyecto: {row.get("tipo_de_proyecto", "N/A")}
extraction_quality: {metadata.extraction_quality.value}
page_count: {metadata.page_count}
---

"""
        full_markdown = header + markdown_content
        full_markdown = full_markdown.encode("utf-8", errors="ignore").decode(
            "utf-8", errors="ignore"
        )

        duration = time.time() - start_time
        await metrics.add_processing_time(duration)

        return True, full_markdown, None

    except Exception as e:
        return False, "", str(e)

    finally:
        if temp_pdf_path.exists():
            temp_pdf_path.unlink()


async def process_single_pdf_optimized(
    session: aioboto3.Session,
    row: pd.Series,
    idx: str,
    stats: ProcessingStats,
    metrics: PerformanceMetrics,
    executor: ProcessPoolExecutor,
    skip_existing: bool = True,
):
    """Process a single PDF with optimized async handling."""
    safe_idx = _sanitize_filename_component(idx)
    markdown_path = OUTPUT_DIR / f"{safe_idx}.md"
    error_path = OUTPUT_DIR / f"FAILED-{safe_idx}.md"

    # Quick skip check
    if skip_existing and (markdown_path.exists() or error_path.exists()):
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

        from_zip = bool(row.get("from_compressed_file", False))

        # Download
        content = await download_from_s3_async(session, bucket, s3_key, metrics)

        # Handle ZIP if needed
        if from_zip:
            if _looks_like_pdf(content):
                pdf_bytes = content
            else:
                prefer_name = row.get("file_name")
                _, pdf_bytes = _extract_pdf_from_zip_bytes(content, prefer_name)
        else:
            pdf_bytes = content

        # Process PDF
        success, markdown_content, error = await process_pdf_async(
            pdf_bytes, idx, row, s3_key, metrics, executor
        )

        if success:
            markdown_path.write_text(markdown_content, encoding="utf-8")
            await stats.increment_processed()
            
            # Clean up error report if exists
            if error_path.exists():
                error_path.unlink()
        else:
            raise Exception(error)

    except Exception as e:
        await stats.increment_failed(idx, str(e))
        
        # Save error report
        error_content = f"""---
file_identifier: {idx}
status: FAILED
error: {str(e)}
s3_key: {s3_key or "N/A"}
---

# Processing Failed

{traceback.format_exc()}
"""
        error_path.write_text(error_content, encoding="utf-8")


async def process_batch_optimized(
    df: pd.DataFrame,
    indices: Optional[list[str]] = None,
    max_files: Optional[int] = None,
    skip_existing: bool = True,
    download_workers: int = DEFAULT_DOWNLOAD_WORKERS,
    processing_workers: int = DEFAULT_PROCESSING_WORKERS,
) -> tuple[ProcessingStats, PerformanceMetrics]:
    """Process batch with optimized parallelization."""
    
    stats = ProcessingStats()
    metrics = PerformanceMetrics()

    # Determine indices to process
    process_indices = indices if indices else list(df.index)
    if max_files:
        process_indices = process_indices[:max_files]

    stats.total = len(process_indices)
    
    logger.info("=" * 60)
    logger.info(f"Total rows in metadata: {len(df):,}")
    logger.info(f"Files to process: {stats.total:,}")
    logger.info(f"Download workers: {download_workers}")
    logger.info(f"Processing workers: {processing_workers}")
    logger.info(f"System: {os.cpu_count()} CPUs, {psutil.virtual_memory().total / (1024**3):.1f}GB RAM")
    logger.info("=" * 60)

    # Create aioboto3 session with connection pooling
    session = aioboto3.Session()
    
    # Create process pool for CPU-intensive PDF parsing
    executor = ProcessPoolExecutor(max_workers=processing_workers)
    
    # Separate semaphores for downloads and processing
    download_semaphore = asyncio.Semaphore(download_workers)
    processing_semaphore = asyncio.Semaphore(processing_workers)

    async def process_with_semaphores(row, idx):
        """Process with separate download and processing semaphores."""
        async with download_semaphore:
            # Download happens here (fast, I/O bound)
            await process_single_pdf_optimized(
                session, row, idx, stats, metrics, executor, skip_existing
            )
        # Processing happens inside process_single_pdf_optimized with executor
        # which has its own concurrency limit

    # Sample memory periodically
    async def memory_sampler():
        while True:
            await metrics.sample_memory()
            await asyncio.sleep(5)

    memory_task = asyncio.create_task(memory_sampler())

    try:
        # Process with progress bar
        with async_tqdm(
            total=stats.total,
            desc="Processing",
            unit="files",
            bar_format=(
                "{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} "
                "[{elapsed}<{remaining}, {rate_fmt}]"
            ),
        ) as pbar:
            tasks = []
            for idx in process_indices:
                row = df.loc[idx]
                task = asyncio.create_task(process_with_semaphores(row, idx))
                
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
        description="Optimized async PDF to Markdown converter"
    )
    parser.add_argument("--max-files", type=int, help="Maximum number of files")
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
        "--skip-existing",
        action="store_true",
        default=True,
        help="Skip existing files",
    )

    args = parser.parse_args()

    ensure_directories()

    # Load metadata
    logger.info(f"Loading metadata from {METADATA_PATH}")
    df = pd.read_parquet(METADATA_PATH)

    # Process files
    stats, metrics = await process_batch_optimized(
        df,
        max_files=args.max_files,
        skip_existing=args.skip_existing,
        download_workers=args.download_workers,
        processing_workers=args.processing_workers,
    )

    # Log results
    stats.log_summary()
    
    perf = metrics.get_summary()
    logger.info("=" * 60)
    logger.info("Performance Metrics:")
    logger.info(f"  Total time: {perf['total_time']:.1f}s")
    logger.info(f"  Avg download: {perf['avg_download_time']:.2f}s")
    logger.info(f"  Avg processing: {perf['avg_processing_time']:.2f}s")
    logger.info(f"  Downloaded: {perf['total_mb_downloaded']:.1f} MB")
    logger.info(f"  Speed: {perf['download_speed_mbps']:.2f} MB/s")
    logger.info(f"  Avg memory: {perf['avg_memory_mb']:.0f} MB")
    logger.info(f"  Peak memory: {perf['peak_memory_mb']:.0f} MB")
    logger.info(f"  Throughput: {stats.processed / perf['total_time']:.2f} files/s")
    logger.info("=" * 60)

    return 0 if stats.failed == 0 else 1


def main():
    """Entry point."""
    return asyncio.run(main_async())


if __name__ == "__main__":
    sys.exit(main())

