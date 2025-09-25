"""Convert SQL metadata to parsed Markdown with async parallel processing.

This script processes PDFs from S3 in parallel using asyncio for efficient concurrent
downloading and parsing. It maintains the same functionality as the synchronous version
but with significantly improved performance through parallelization.

Run it using uv:

uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py
"""

# %%
from __future__ import annotations

import asyncio
import logging
import sys
import tempfile
import time
import traceback
import zipfile
from dataclasses import dataclass, field
from io import BytesIO
from pathlib import Path
from typing import Optional

import pandas as pd
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
    print("Installing aioboto3 for async S3 operations...")
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
        logging.FileHandler("SimpleWorkflow/processing_async.log", mode="a"),
    ],
)
logger = logging.getLogger(__name__)

# Constants
METADATA_PATH = "sql/metadata_table/flora_fauna_metadata_indexed.parquet"
OUTPUT_DIR = Path("SimpleWorkflow/ParsedFiles")
TEMP_DIR = Path(tempfile.gettempdir()) / "pdf_processing_async"
MAX_RETRIES = 3  # Maximum retries for S3 operations
RETRY_DELAY = 2  # Seconds to wait between retries
MAX_CONCURRENT_WORKERS = 5  # Default number of concurrent workers


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

        if self.errors:
            logger.error("Failed files:")
            for idx, error in self.errors[:10]:  # Show first 10 errors
                logger.error(f"  - {idx}: {error}")
            if len(self.errors) > 10:
                logger.error(f"  ... and {len(self.errors) - 10} more")


def ensure_directories():
    """Ensure required directories exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory: {OUTPUT_DIR}")
    logger.info(f"Temp directory: {TEMP_DIR}")


def _extract_pdf_from_zip_bytes(
    zip_bytes: bytes, prefer_name: Optional[str] = None
) -> tuple[str, bytes]:
    """Extract a PDF file from ZIP archive bytes.

    Args:
        zip_bytes: The ZIP file content as bytes
        prefer_name: Preferred PDF filename to extract if multiple exist

    Returns:
        Tuple of (pdf_filename, pdf_bytes)

    Raises:
        ValueError: If no PDF found in the ZIP
    """
    with zipfile.ZipFile(BytesIO(zip_bytes), "r") as zf:
        # Get all PDF files in the ZIP
        pdf_files = [
            name
            for name in zf.namelist()
            if name.lower().endswith(".pdf") and not name.startswith("__MACOSX")
        ]

        if not pdf_files:
            raise ValueError("No PDF files found in ZIP archive")

        # Select which PDF to extract
        if prefer_name and prefer_name in pdf_files:
            selected_pdf = prefer_name
        elif len(pdf_files) == 1:
            selected_pdf = pdf_files[0]
        else:
            # Pick the largest PDF if multiple exist
            sizes = {name: zf.getinfo(name).file_size for name in pdf_files}
            selected_pdf = max(sizes, key=sizes.get)
            logger.info(f"Multiple PDFs found, selecting largest: {selected_pdf}")

        # Extract and return the PDF
        pdf_bytes = zf.read(selected_pdf)
        return selected_pdf, pdf_bytes


def save_error_markdown(
    index_value: str,
    error: Exception,
    row: pd.Series,
    s3_key: str = None,
) -> None:
    """Save error details to a markdown file for debugging."""
    safe_index = _sanitize_filename_component(index_value)
    error_path = OUTPUT_DIR / f"FAILED-{safe_index}.md"

    # Create error markdown content
    error_content = f"""---
file_identifier: {index_value}
status: FAILED
error_type: {type(error).__name__}
error_time: {pd.Timestamp.now().isoformat()}
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
5. If the file is corrupted, consider re-downloading from source

---
*This error report was automatically generated*
"""

    try:
        error_path.write_text(error_content, encoding="utf-8")
        logger.debug(f"Saved error report: {error_path}")
    except Exception as e:
        logger.error(f"Failed to save error report for {index_value}: {e}")


async def download_from_s3_async(
    session, bucket: str, key: str, max_retries: int = MAX_RETRIES
) -> bytes:
    """Download file from S3 asynchronously with retry logic.

    Args:
        session: aioboto3 session
        bucket: S3 bucket name
        key: S3 object key
        max_retries: Maximum number of retry attempts

    Returns:
        File content as bytes

    Raises:
        Exception: If download fails after all retries
    """
    for attempt in range(max_retries):
        try:
            async with session.client("s3") as s3:
                response = await s3.get_object(Bucket=bucket, Key=key)
                content = await response["Body"].read()
                return content
        except Exception as e:
            if attempt < max_retries - 1:
                logger.warning(
                    f"Download attempt {attempt + 1} failed for {key}, retrying: {e}"
                )
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))  # Exponential backoff
            else:
                raise Exception(
                    f"Failed to download {key} after {max_retries} attempts: {e}"
                )


async def process_pdf_async(
    pdf_bytes: bytes, index_value: str, row: pd.Series, s3_key: str
) -> tuple[bool, str, Optional[str]]:
    """Process PDF bytes and convert to markdown asynchronously.

    Args:
        pdf_bytes: PDF content as bytes
        index_value: The index identifier for the file
        row: Metadata row from the dataframe
        s3_key: S3 key for metadata

    Returns:
        Tuple of (success, markdown_content, error_message)
    """
    safe_index = _sanitize_filename_component(index_value)
    temp_pdf_path = TEMP_DIR / f"{safe_index}.pdf"

    try:
        # Write PDF to temporary file
        temp_pdf_path.write_bytes(pdf_bytes)

        file_size_mb = len(pdf_bytes) / (1024 * 1024)
        logger.debug(f"PDF file size for {index_value}: {file_size_mb:.2f} MB")

        if file_size_mb > 100:  # Warn for large files
            logger.warning(
                f"Large PDF file ({file_size_mb:.2f} MB) for {index_value}, processing may take time"
            )

        # Run PDF parsing in executor to avoid blocking
        loop = asyncio.get_event_loop()

        # Create a wrapper function with the correct arguments
        def parse_pdf():
            return extract_markdown(
                temp_pdf_path,
                output_dir=None,
                ignore_images=True,
                clean_text=True,
                validate_quality=True,
                show_progress=False,
            )

        markdown_content, metadata = await loop.run_in_executor(None, parse_pdf)

        # Add metadata header to markdown
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

        # Clean up problematic Unicode characters
        full_markdown = full_markdown.encode("utf-8", errors="ignore").decode(
            "utf-8", errors="ignore"
        )

        return True, full_markdown, None

    except Exception as e:
        error_msg = f"Failed to process PDF for {index_value}: {str(e)}"
        logger.error(error_msg)
        return False, None, str(e)

    finally:
        # Clean up temporary PDF
        if temp_pdf_path.exists():
            temp_pdf_path.unlink()


async def process_single_pdf_async(
    session,
    row: pd.Series,
    index_value: str,
    stats: ProcessingStats,
    pbar: async_tqdm,
    skip_existing: bool = True,
) -> None:
    """Process a single PDF asynchronously.

    Args:
        session: aioboto3 session
        row: Metadata row from the dataframe
        index_value: The index identifier for the file
        stats: ProcessingStats object to track progress
        pbar: Progress bar object
        skip_existing: Skip if markdown already exists
    """
    # Build output path for markdown
    safe_index = _sanitize_filename_component(index_value)
    markdown_path = OUTPUT_DIR / f"{safe_index}.md"
    error_path = OUTPUT_DIR / f"FAILED-{safe_index}.md"

    # Skip if already exists
    if skip_existing and (markdown_path.exists() or error_path.exists()):
        await stats.increment_skipped()
        pbar.set_postfix_str(
            f"✓{stats.processed} ⏭{stats.skipped} ✗{stats.failed}", refresh=False
        )
        return

    s3_key = None
    try:
        # Resolve S3 bucket and key
        bucket, s3_key = _resolve_bucket_and_key(row)

        # Skip macOS system files
        if "__MACOSX" in s3_key or "/._" in s3_key or s3_key.startswith("._"):
            logger.debug(f"Skipping macOS system file: {s3_key}")
            await stats.increment_skipped()
            pbar.set_postfix_str(
                f"✓{stats.processed} ⏭{stats.skipped} ✗{stats.failed}", refresh=False
            )
            return

        # Download from S3
        logger.debug(f"Downloading {index_value} from s3://{bucket}/{s3_key}")
        content = await download_from_s3_async(session, bucket, s3_key)

        # Check if it's from a compressed file (ZIP)
        from_zip = bool(row.get("from_compressed_file", False))

        if from_zip:
            # Check if it's actually a PDF (mismarked as compressed)
            if _looks_like_pdf(content):
                logger.debug(
                    f"File {index_value} marked as compressed but is actually a PDF"
                )
                pdf_bytes = content
            else:
                # Extract PDF from ZIP
                prefer_name = row.get("file_name")
                internal_name, pdf_bytes = _extract_pdf_from_zip_bytes(
                    content, prefer_name=prefer_name
                )
                logger.debug(f"Extracted '{internal_name}' from ZIP for {index_value}")
        else:
            pdf_bytes = content

        # Process PDF to markdown
        success, markdown_content, error_msg = await process_pdf_async(
            pdf_bytes, index_value, row, s3_key
        )

        if success:
            # Save markdown file
            markdown_path.write_text(markdown_content, encoding="utf-8")
            logger.info(f"✓ Processed: {index_value}")
            await stats.increment_processed()
        else:
            # Save error report
            error = Exception(error_msg)
            save_error_markdown(index_value, error, row, s3_key)
            await stats.increment_failed(index_value, error_msg)

        pbar.set_postfix_str(
            f"✓{stats.processed} ⏭{stats.skipped} ✗{stats.failed}", refresh=False
        )

    except Exception as e:
        logger.error(f"Failed to process {index_value}: {str(e)}")
        save_error_markdown(index_value, e, row, s3_key)
        await stats.increment_failed(index_value, str(e))
        pbar.set_postfix_str(
            f"✓{stats.processed} ⏭{stats.skipped} ✗{stats.failed}", refresh=False
        )


async def process_batch_async(
    df: pd.DataFrame,
    indices: Optional[list[str]] = None,
    max_files: Optional[int] = None,
    skip_existing: bool = True,
    dry_run: bool = False,
    max_workers: int = MAX_CONCURRENT_WORKERS,
) -> ProcessingStats:
    """Process a batch of PDFs asynchronously.

    Args:
        df: Metadata dataframe
        indices: Specific indices to process (None for all)
        max_files: Maximum number of files to process
        skip_existing: Skip files that already have markdown
        dry_run: If True, only show what would be processed
        max_workers: Maximum number of concurrent workers

    Returns:
        ProcessingStats with results
    """
    stats = ProcessingStats()

    # Determine which indices to process
    if indices:
        process_indices = indices
    else:
        process_indices = list(df.index)

    # Display total rows in the dataframe
    total_rows_in_df = len(df)
    logger.info("=" * 60)
    logger.info(f"Total rows in metadata: {total_rows_in_df:,}")

    # Limit if max_files specified
    if max_files:
        process_indices = process_indices[:max_files]
        logger.info(f"Limited to processing: {max_files:,} files")

    stats.total = len(process_indices)
    logger.info(f"Files to process: {stats.total:,}")
    logger.info(f"Parallel workers: {max_workers}")
    logger.info("=" * 60)

    if dry_run:
        logger.info("[DRY RUN MODE] - No files will be processed")

        # Count how many would be skipped
        would_skip = 0
        would_skip_failed = 0
        would_process = 0

        for idx in process_indices:
            safe_idx = _sanitize_filename_component(idx)
            markdown_path = OUTPUT_DIR / f"{safe_idx}.md"
            error_path = OUTPUT_DIR / f"FAILED-{safe_idx}.md"

            if skip_existing and markdown_path.exists():
                would_skip += 1
            elif skip_existing and error_path.exists():
                would_skip_failed += 1
            else:
                would_process += 1

        logger.info(f"  Would process: {would_process} new files")
        logger.info(f"  Would skip: {would_skip} existing files")
        if would_skip_failed > 0:
            logger.info(f"  Would skip: {would_skip_failed} previously failed files")

        stats.total = len(process_indices)
        stats.skipped = would_skip
        return stats

    # Create aioboto3 session
    session = aioboto3.Session()

    # Create semaphore to limit concurrent operations
    semaphore = asyncio.Semaphore(max_workers)

    async def process_with_semaphore(row, idx, pbar):
        async with semaphore:
            await process_single_pdf_async(
                session, row, idx, stats, pbar, skip_existing=skip_existing
            )
            pbar.update(1)

    # Process files with async progress bar
    with async_tqdm(
        total=stats.total,
        desc="Processing",
        unit="files",
        bar_format=(
            "{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} "
            "[{elapsed}<{remaining}, {rate_fmt}]"
        ),
        ncols=100,
        dynamic_ncols=True,
    ) as pbar:
        # Create tasks for all files
        tasks = []
        for idx in process_indices:
            row = df.loc[idx]
            task = asyncio.create_task(process_with_semaphore(row, idx, pbar))
            tasks.append(task)

        # Wait for all tasks to complete
        await asyncio.gather(*tasks, return_exceptions=True)

    return stats


def verify_naming_convention(df: pd.DataFrame) -> tuple[bool, list[str]]:
    """Verify that existing files match the dataframe index naming convention."""
    if not OUTPUT_DIR.exists():
        return True, []

    mismatched_files = []
    existing_files = list(OUTPUT_DIR.glob("*.md"))

    logger.info(f"Verifying naming convention for {len(existing_files)} existing files")

    for file_path in existing_files:
        filename = file_path.stem  # Get filename without extension

        # Skip FAILED- files in this check
        if filename.startswith("FAILED-"):
            continue

        # Check if the filename exists in the dataframe index
        if filename not in df.index:
            # Try to find if it's a sanitized version
            found = False
            for idx in df.index:
                if _sanitize_filename_component(idx) == filename:
                    found = True
                    break

            if not found:
                mismatched_files.append(file_path.name)
                logger.warning(
                    f"File '{file_path.name}' does not match any index in metadata"
                )

    if mismatched_files:
        logger.error(
            f"Found {len(mismatched_files)} files that don't match the naming convention:"
        )
        for file in mismatched_files[:10]:  # Show first 10
            logger.error(f"  - {file}")
        if len(mismatched_files) > 10:
            logger.error(f"  ... and {len(mismatched_files) - 10} more")
        return False, mismatched_files
    else:
        logger.info("✓ All existing files match the naming convention")
        return True, []


async def main_async():
    """Main async execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert PDFs from S3 to Markdown using async parallel processing"
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
        "--dry-run",
        action="store_true",
        help="Show what would be processed without actually doing it",
    )
    parser.add_argument(
        "--sample",
        type=int,
        help="Process a random sample of N files",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=MAX_CONCURRENT_WORKERS,
        help=f"Number of parallel workers (default: {MAX_CONCURRENT_WORKERS})",
    )

    args = parser.parse_args()

    # Ensure directories exist
    ensure_directories()

    # Load metadata
    logger.info(f"Loading metadata from {METADATA_PATH}")
    try:
        df = pd.read_parquet(METADATA_PATH)
        logger.info("=" * 60)
        logger.info("✓ Successfully loaded metadata")
        logger.info(f"  Total rows in parquet file: {len(df):,}")
        logger.info(
            f"  Columns: {', '.join(df.columns[:5])}"
            + (f", ... ({len(df.columns)} total)" if len(df.columns) > 5 else "")
        )
        logger.info("=" * 60)
    except Exception as e:
        logger.error(f"Failed to load metadata: {e}")
        sys.exit(1)

    # Verify naming convention
    naming_valid, mismatched = verify_naming_convention(df)
    if not naming_valid and not args.dry_run:
        logger.warning(
            f"Found {len(mismatched)} files that don't match the naming convention. "
            "Consider reviewing or removing these files."
        )
        # Ask for confirmation to continue
        if sys.stdin.isatty():  # Check if running interactively
            response = (
                input("\nDo you want to continue anyway? (y/N): ").strip().lower()
            )
            if response != "y":
                logger.info("Aborting due to naming convention mismatch")
                sys.exit(1)
        else:
            logger.warning("Non-interactive mode, continuing despite mismatches")

    # Handle sample mode
    if args.sample:
        logger.info(f"Sampling {args.sample} random files")
        sample_indices = df.sample(n=min(args.sample, len(df))).index.tolist()
        args.indices = sample_indices
        args.max_files = None

    # Process files asynchronously
    start_time = time.time()
    stats = await process_batch_async(
        df,
        indices=args.indices,
        max_files=args.max_files,
        skip_existing=args.skip_existing,
        dry_run=args.dry_run,
        max_workers=args.workers,
    )
    elapsed = time.time() - start_time

    # Log summary
    stats.log_summary()
    if stats.processed > 0:
        logger.info(f"Processing time: {elapsed:.2f} seconds")
        logger.info(f"Average speed: {stats.processed / elapsed:.2f} files/second")

    # Clean up temp directory if empty
    if TEMP_DIR.exists() and not any(TEMP_DIR.iterdir()):
        TEMP_DIR.rmdir()
        logger.info("Cleaned up empty temp directory")

    return 0 if stats.failed == 0 else 1


def main():
    """Entry point for the async script."""
    return asyncio.run(main_async())


if __name__ == "__main__":
    sys.exit(main())
