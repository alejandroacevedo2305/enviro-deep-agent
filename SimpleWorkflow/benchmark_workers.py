"""Benchmark script to find optimal worker configuration.

This script tests different worker configurations to find the best performance
for your specific system and network conditions.

Usage:
uv run python SimpleWorkflow/benchmark_workers.py --sample 50
"""

# %%
from __future__ import annotations

import asyncio
import sys
import time
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))

from sql_metadata_to_parsed_markdown_optimized import (
    METADATA_PATH,
    ensure_directories,
    logger,
    process_batch_optimized,
)


async def benchmark_configuration(
    df: pd.DataFrame,
    sample_size: int,
    download_workers: int,
    processing_workers: int,
) -> dict:
    """Benchmark a specific worker configuration."""

    # Sample random files
    sample_indices = df.sample(n=sample_size).index.tolist()

    logger.info("=" * 70)
    logger.info(
        f"Testing: {download_workers} download workers, "
        f"{processing_workers} processing workers"
    )

    start_time = time.time()

    stats, metrics = await process_batch_optimized(
        df,
        indices=sample_indices,
        skip_existing=False,  # Force reprocess for fair comparison
        download_workers=download_workers,
        processing_workers=processing_workers,
    )

    elapsed = time.time() - start_time
    perf = metrics.get_summary()

    return {
        "download_workers": download_workers,
        "processing_workers": processing_workers,
        "total_time": elapsed,
        "files_processed": stats.processed,
        "files_failed": stats.failed,
        "throughput": stats.processed / elapsed if elapsed > 0 else 0,
        "avg_download_time": perf["avg_download_time"],
        "avg_processing_time": perf["avg_processing_time"],
        "peak_memory_mb": perf["peak_memory_mb"],
        "score": (stats.processed / elapsed) if elapsed > 0 else 0,
    }


async def run_benchmark(sample_size: int = 50):
    """Run benchmark with different worker configurations."""

    ensure_directories()

    logger.info("Loading metadata...")
    df = pd.read_parquet(METADATA_PATH)

    # Test configurations
    # Format: (download_workers, processing_workers)
    configs = [
        (5, 2),  # Conservative
        (10, 3),  # Balanced
        (15, 4),  # Aggressive
        (20, 5),  # Very aggressive
        (10, 2),  # I/O heavy
        (5, 4),  # CPU heavy
    ]

    results = []

    logger.info("=" * 70)
    logger.info(f"Starting benchmark with {sample_size} files per configuration")
    logger.info("=" * 70)

    for download_w, processing_w in configs:
        try:
            result = await benchmark_configuration(
                df, sample_size, download_w, processing_w
            )
            results.append(result)

            logger.info(f"✓ Result: {result['throughput']:.2f} files/sec")

        except Exception as e:
            logger.error(f"✗ Configuration failed: {e}")
            results.append(
                {
                    "download_workers": download_w,
                    "processing_workers": processing_w,
                    "score": 0,
                    "error": str(e),
                }
            )

    # Find best configuration
    results.sort(key=lambda x: x.get("score", 0), reverse=True)

    logger.info("=" * 70)
    logger.info("BENCHMARK RESULTS")
    logger.info("=" * 70)

    for i, result in enumerate(results, 1):
        if result.get("score", 0) > 0:
            logger.info(f"\n#{i} Configuration:")
            logger.info(f"  Download workers: {result['download_workers']}")
            logger.info(f"  Processing workers: {result['processing_workers']}")
            logger.info(f"  Throughput: {result['throughput']:.2f} files/sec")
            logger.info(f"  Total time: {result['total_time']:.1f}s")
            logger.info(f"  Success rate: {result['files_processed']}/{sample_size}")
            logger.info(f"  Avg download: {result['avg_download_time']:.2f}s")
            logger.info(f"  Avg processing: {result['avg_processing_time']:.2f}s")
            logger.info(f"  Peak memory: {result['peak_memory_mb']:.0f} MB")

    logger.info("=" * 70)
    logger.info("RECOMMENDATION")
    logger.info("=" * 70)

    best = results[0]
    logger.info("Best configuration:")
    logger.info(
        f"  --download-workers {best['download_workers']} "
        f"--processing-workers {best['processing_workers']}"
    )
    logger.info(f"  Expected throughput: {best['throughput']:.2f} files/sec")

    # Generate command
    logger.info("\nRecommended command:")
    logger.info(
        f"  uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py "
        f"--download-workers {best['download_workers']} "
        f"--processing-workers {best['processing_workers']}"
    )


def main():
    """Entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Benchmark worker configurations")
    parser.add_argument(
        "--sample",
        type=int,
        default=50,
        help="Number of files to test per configuration (default: 50)",
    )

    args = parser.parse_args()

    asyncio.run(run_benchmark(args.sample))


if __name__ == "__main__":
    main()
