"""Optimizer script to find optimal worker configuration for retry_failed_files.

This script benchmarks different worker configurations to find the best
performance for retrying failed PDF parsing on your specific system and network
conditions.

The optimizer:
- Tests multiple worker configurations (conservative to aggressive)
- Measures throughput, memory usage, and processing times
- Provides a ranked list of configurations
- Shows the optimal command to use

Usage:
    # Test with actual failed files (dry-run, doesn't modify files)
    uv run python SimpleWorkflow/optimize_retry_workers.py

    # Test with a custom sample size (if you have many failed files)
    uv run python SimpleWorkflow/optimize_retry_workers.py --sample 20

    # Skip configurations that exceed memory limits
    uv run python SimpleWorkflow/optimize_retry_workers.py --max-memory 80

Features:
- Intelligent configuration selection based on system resources
- Memory-aware benchmarking (stops if memory usage is too high)
- Detailed performance metrics for each configuration
- Generates optimized command ready to run
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
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(
            "SimpleWorkflow/optimize_retry_workers.log",
            mode="w",
        ),
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


@dataclass
class BenchmarkMetrics:
    """Track detailed benchmark metrics."""

    start_time: float = field(default_factory=time.time)
    download_times: list[float] = field(default_factory=list)
    processing_times: list[float] = field(default_factory=list)
    total_bytes_downloaded: int = 0
    memory_samples: list[float] = field(default_factory=list)
    success_count: int = 0
    failed_count: int = 0
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

    async def increment_success(self):
        async with self.lock:
            self.success_count += 1

    async def increment_failed(self):
        async with self.lock:
            self.failed_count += 1

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
            "peak_memory_mb": (
                max(self.memory_samples) if self.memory_samples else 0
            ),
            "success_count": self.success_count,
            "failed_count": self.failed_count,
            "throughput": (
                self.success_count / elapsed if elapsed > 0 else 0
            ),
        }


def parse_failed_file_metadata(failed_file_path: Path) -> Optional[dict]:
    """Parse metadata from a FAILED-*.md file."""
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
    except Exception:
        return None


def find_failed_files() -> list[tuple[Path, dict]]:
    """Find all FAILED-*.md files and parse their metadata."""
    failed_files = []

    for failed_path in OUTPUT_DIR.glob("FAILED-*.md"):
        metadata = parse_failed_file_metadata(failed_path)
        if metadata:
            failed_files.append((failed_path, metadata))

    return failed_files


async def download_from_s3_async(
    session: aioboto3.Session,
    bucket: str,
    s3_key: str,
    metrics: BenchmarkMetrics,
    max_retries: int = MAX_RETRIES,
) -> bytes:
    """Download file from S3 asynchronously with retries and metrics."""
    start_time = time.time()

    for attempt in range(max_retries):
        try:
            async with session.client("s3") as s3_client:
                response = await s3_client.get_object(
                    Bucket=bucket,
                    Key=s3_key,
                )
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
    """Worker function for PDF extraction (must be picklable)."""
    try:
        markdown_text, _metadata = extract_markdown(pdf_path_str)
        return markdown_text, None
    except Exception as exc:
        return "", exc


async def process_pdf_async(
    pdf_bytes: bytes,
    file_identifier: str,
    executor: ProcessPoolExecutor,
    metrics: BenchmarkMetrics,
) -> tuple[bool, str, Optional[str]]:
    """Process PDF bytes to markdown asynchronously (dry-run)."""
    start_time = time.time()
    temp_dir = Path("SimpleWorkflow/.temp_benchmark")
    temp_dir.mkdir(parents=True, exist_ok=True)

    safe_name = _sanitize_filename_component(file_identifier)
    temp_pdf_path = temp_dir / f"{safe_name}.pdf"

    try:
        # Write PDF to temp file
        temp_pdf_path.write_bytes(pdf_bytes)

        # Extract markdown using process pool
        loop = asyncio.get_event_loop()
        markdown, error = await loop.run_in_executor(
            executor,
            extract_markdown_worker,
            str(temp_pdf_path),
        )

        if error:
            return False, "", str(error)

        duration = time.time() - start_time
        await metrics.add_processing_time(duration)

        return True, markdown, None

    except Exception as exc:
        return False, "", str(exc)
    finally:
        # Clean up temp file
        if temp_pdf_path.exists():
            try:
                temp_pdf_path.unlink()
            except Exception:
                pass


async def benchmark_single_file(
    session: aioboto3.Session,
    metadata: dict,
    df_metadata: pd.DataFrame,
    executor: ProcessPoolExecutor,
    metrics: BenchmarkMetrics,
) -> bool:
    """Benchmark processing a single failed file (dry-run, no file changes)."""
    file_identifier = metadata["file_identifier"]
    s3_key = metadata["s3_key"]

    try:
        # Try to get additional info from metadata DataFrame
        if file_identifier in df_metadata.index:
            row = df_metadata.loc[file_identifier]
            bucket, s3_key = _resolve_bucket_and_key(row)
        else:
            # Extract bucket from s3_key
            if s3_key.startswith("s3://"):
                parts = s3_key[5:].split("/", 1)
                bucket = parts[0]
                s3_key = parts[1]
            else:
                bucket = "sea-crawler"

        # Download from S3
        pdf_bytes = await download_from_s3_async(
            session,
            bucket,
            s3_key,
            metrics,
        )

        # Check for empty files
        if len(pdf_bytes) == 0:
            raise ValueError("Empty file (0 bytes)")

        # Remove UTF-8 BOM if present
        if pdf_bytes.startswith(b"\xef\xbb\xbf"):
            pdf_bytes = pdf_bytes[3:]

        # Verify it's actually a PDF
        if not pdf_bytes.startswith(b"%PDF"):
            raise ValueError(
                f"Not a PDF file (starts with: {pdf_bytes[:20]!r})"
            )

        # Process PDF to markdown (dry-run, don't save)
        success, _markdown_content, error_msg = await process_pdf_async(
            pdf_bytes,
            file_identifier,
            executor,
            metrics,
        )

        if not success:
            raise RuntimeError(f"Markdown extraction failed: {error_msg}")

        await metrics.increment_success()
        return True

    except Exception:
        await metrics.increment_failed()
        return False


async def benchmark_configuration(
    download_workers: int,
    processing_workers: int,
    failed_files: list[tuple[Path, dict]],
    df_metadata: pd.DataFrame,
    sample_size: int,
    max_memory_percent: float = 80.0,
) -> dict:
    """Benchmark a specific worker configuration."""
    logger.info("=" * 70)
    logger.info(
        "Testing: %d download workers, %d processing workers",
        download_workers,
        processing_workers,
    )

    # Initialize metrics
    metrics = BenchmarkMetrics()

    # Sample files to test
    import random

    sample_files = (
        random.sample(failed_files, min(sample_size, len(failed_files)))
        if len(failed_files) > sample_size
        else failed_files
    )

    # Create async S3 session
    s3_config = S3Config.from_env()
    session_kwargs = {}
    if s3_config.region_name:
        session_kwargs["region_name"] = s3_config.region_name

    session = aioboto3.Session(**session_kwargs)

    # Create process pool
    executor = ProcessPoolExecutor(max_workers=processing_workers)

    # Download semaphore
    download_semaphore = asyncio.Semaphore(download_workers)

    async def benchmark_with_semaphore(_failed_path: Path, metadata: dict):
        """Benchmark with download semaphore."""
        async with download_semaphore:
            await benchmark_single_file(
                session,
                metadata,
                df_metadata,
                executor,
                metrics,
            )

    # Memory monitoring
    memory_exceeded = False

    async def memory_monitor():
        nonlocal memory_exceeded
        while True:
            await metrics.sample_memory()
            memory_percent = psutil.virtual_memory().percent
            if memory_percent > max_memory_percent:
                logger.warning(
                    "Memory usage exceeded %.1f%% threshold",
                    max_memory_percent,
                )
                memory_exceeded = True
                break
            await asyncio.sleep(2)

    memory_task = asyncio.create_task(memory_monitor())

    try:
        # Process with progress bar
        with tqdm(
            total=len(sample_files),
            desc="Benchmarking",
            unit="files",
            leave=False,
            disable=True,  # Disable for cleaner output
        ) as pbar:
            tasks = []
            for failed_path, metadata in sample_files:
                if memory_exceeded:
                    break

                task = asyncio.create_task(
                    benchmark_with_semaphore(failed_path, metadata)
                )
                task.add_done_callback(lambda _: pbar.update(1))
                tasks.append(task)

                # Batch task creation
                if len(tasks) >= download_workers * 2:
                    await asyncio.gather(*tasks, return_exceptions=True)
                    tasks = []
                    gc.collect()

            # Wait for remaining tasks
            if tasks and not memory_exceeded:
                await asyncio.gather(*tasks, return_exceptions=True)

    finally:
        memory_task.cancel()
        executor.shutdown(wait=True)

        # Cleanup temp directory
        temp_dir = Path("SimpleWorkflow/.temp_benchmark")
        if temp_dir.exists():
            import shutil

            try:
                shutil.rmtree(temp_dir)
            except Exception:
                pass

    # Get performance summary
    perf = metrics.get_summary()

    result = {
        "download_workers": download_workers,
        "processing_workers": processing_workers,
        "total_time": perf["total_time"],
        "files_processed": perf["success_count"],
        "files_failed": perf["failed_count"],
        "throughput": perf["throughput"],
        "avg_download_time": perf["avg_download_time"],
        "avg_processing_time": perf["avg_processing_time"],
        "peak_memory_mb": perf["peak_memory_mb"],
        "download_speed_mbps": perf["download_speed_mbps"],
        "memory_exceeded": memory_exceeded,
        "score": (
            perf["throughput"]
            if not memory_exceeded and perf["success_count"] > 0
            else 0
        ),
    }

    logger.info(
        "✓ Result: %.2f files/sec | Peak memory: %.0f MB",
        result["throughput"],
        result["peak_memory_mb"],
    )

    return result


def generate_test_configurations() -> list[tuple[int, int]]:
    """Generate test configurations based on system resources."""
    cpu_count = os.cpu_count() or 4
    memory_gb = psutil.virtual_memory().total / (1024**3)

    # Calculate reasonable ranges
    max_download_workers = min(cpu_count * 3, int(memory_gb * 2), 30)
    max_processing_workers = min(max(cpu_count - 1, 2), int(memory_gb / 2), 12)

    # Generate configurations from conservative to aggressive
    configs = []

    # Conservative
    configs.append((5, 2))

    # Balanced configurations
    for download in [10, 15, 20]:
        for processing in [2, 3, 4]:
            if (
                download <= max_download_workers
                and processing <= max_processing_workers
            ):
                configs.append((download, processing))

    # Aggressive configurations
    if max_download_workers >= 25:
        for processing in [4, 5, 6]:
            if processing <= max_processing_workers:
                configs.append((25, processing))

    if max_download_workers >= 30:
        for processing in [5, 6, 8]:
            if processing <= max_processing_workers:
                configs.append((30, processing))

    # I/O heavy vs CPU heavy
    configs.append((max_download_workers, 2))
    configs.append((10, max_processing_workers))

    # Remove duplicates and sort
    configs = list(set(configs))
    configs.sort()

    return configs


async def run_optimization(
    sample_size: int = 30,
    max_memory_percent: float = 80.0,
):
    """Run optimization benchmark with different worker configurations."""
    logger.info("=" * 70)
    logger.info("RETRY FAILED FILES - WORKER OPTIMIZATION")
    logger.info("=" * 70)
    logger.info("")

    # System info
    cpu_count = os.cpu_count() or 4
    memory_gb = psutil.virtual_memory().total / (1024**3)
    logger.info("System Information:")
    logger.info("  CPUs: %d", cpu_count)
    logger.info("  RAM: %.1f GB", memory_gb)
    logger.info("  Max memory threshold: %.1f%%", max_memory_percent)
    logger.info("")

    # Find failed files
    logger.info("Scanning for failed files...")
    failed_files = find_failed_files()

    if not failed_files:
        logger.error("No failed files found to optimize with!")
        logger.error("Please run the main processing script first to generate")
        logger.error("some failed files, then retry this optimizer.")
        return

    logger.info("Found %d failed files", len(failed_files))
    test_sample = min(sample_size, len(failed_files))
    logger.info("Will test with %d files per configuration", test_sample)
    logger.info("")

    # Load metadata
    logger.info("Loading metadata...")
    try:
        df_metadata = load_metadata(PARQUET_PATH)
        logger.info("✓ Loaded metadata with %d rows", len(df_metadata))
    except Exception as exc:
        logger.error("✗ Failed to load metadata: %s", exc)
        return

    logger.info("")

    # Generate test configurations
    configs = generate_test_configurations()
    logger.info("Testing %d configurations...", len(configs))
    logger.info("")

    # Run benchmarks
    results = []
    for download_w, processing_w in configs:
        try:
            result = await benchmark_configuration(
                download_w,
                processing_w,
                failed_files,
                df_metadata,
                test_sample,
                max_memory_percent,
            )
            results.append(result)

        except Exception as exc:
            logger.error(
                "✗ Configuration (%d, %d) failed: %s",
                download_w,
                processing_w,
                exc,
            )
            results.append(
                {
                    "download_workers": download_w,
                    "processing_workers": processing_w,
                    "score": 0,
                    "error": str(exc),
                }
            )

        # Small delay between tests
        await asyncio.sleep(1)
        gc.collect()

    # Sort by score
    results.sort(key=lambda x: x.get("score", 0), reverse=True)

    # Display results
    logger.info("")
    logger.info("=" * 70)
    logger.info("OPTIMIZATION RESULTS")
    logger.info("=" * 70)
    logger.info("")

    for i, result in enumerate(results[:10], 1):  # Show top 10
        if result.get("score", 0) > 0:
            logger.info("#%d Configuration:", i)
            logger.info(
                "  Download workers: %d",
                result["download_workers"],
            )
            logger.info(
                "  Processing workers: %d",
                result["processing_workers"],
            )
            logger.info("  Throughput: %.2f files/sec", result["throughput"])
            logger.info("  Total time: %.1fs", result["total_time"])
            logger.info(
                "  Success rate: %d/%d",
                result["files_processed"],
                test_sample,
            )
            logger.info(
                "  Avg download: %.2fs",
                result["avg_download_time"],
            )
            logger.info(
                "  Avg processing: %.2fs",
                result["avg_processing_time"],
            )
            logger.info(
                "  Peak memory: %.0f MB",
                result["peak_memory_mb"],
            )
            logger.info(
                "  Download speed: %.2f MB/s",
                result["download_speed_mbps"],
            )
            logger.info("")

    # Show recommendation
    logger.info("=" * 70)
    logger.info("RECOMMENDATION")
    logger.info("=" * 70)
    logger.info("")

    if results and results[0].get("score", 0) > 0:
        best = results[0]
        logger.info("✓ Optimal configuration found:")
        logger.info(
            "  Download workers: %d",
            best["download_workers"],
        )
        logger.info(
            "  Processing workers: %d",
            best["processing_workers"],
        )
        logger.info(
            "  Expected throughput: %.2f files/sec",
            best["throughput"],
        )
        logger.info(
            "  Estimated time for %d failed files: %.1f minutes",
            len(failed_files),
            (len(failed_files) / best["throughput"]) / 60,
        )
        logger.info("")
        logger.info("Recommended command:")
        logger.info(
            "  uv run python SimpleWorkflow/retry_failed_files.py \\"
        )
        logger.info(
            "    --download-workers %d \\",
            best["download_workers"],
        )
        logger.info(
            "    --processing-workers %d",
            best["processing_workers"],
        )
        logger.info("")
        logger.info("Or run in background:")
        logger.info(
            "  nohup uv run python SimpleWorkflow/retry_failed_files.py \\"
        )
        logger.info(
            "    --download-workers %d \\",
            best["download_workers"],
        )
        logger.info(
            "    --processing-workers %d \\",
            best["processing_workers"],
        )
        logger.info(
            "    > SimpleWorkflow/retry_processing.log 2>&1 &"
        )
    else:
        logger.error("✗ No successful configurations found!")

    logger.info("=" * 70)


async def main_async():
    """Main async execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Optimize retry_failed_files worker configuration for maximum "
            "throughput"
        )
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=30,
        help="Number of files to test per configuration (default: 30)",
    )
    parser.add_argument(
        "--max-memory",
        type=float,
        default=80.0,
        help="Max memory usage percent before stopping test (default: 80.0)",
    )

    args = parser.parse_args()

    await run_optimization(
        sample_size=args.sample,
        max_memory_percent=args.max_memory,
    )


def main():
    """Entry point."""
    return asyncio.run(main_async())


if __name__ == "__main__":
    sys.exit(main())

