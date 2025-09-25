"""Convert SQL metadata to parsed Markdown.

This script goes over each row of the dataframe
sql/metadata_table/flora_fauna_metadata_indexed.parquet, downloads PDFs from the S3
bucket, converts them to Markdown using localPDFparse.parse.extract_markdown, and saves
the results to SimpleWorkflow/ParsedFiles.

The script preserves the naming convention from s3pdf_manager, downloads PDFs to a
temporary directory, processes them, and cleans up afterward.

run it using uv:

uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py
"""

# %%
from __future__ import annotations

import logging
import sys
import tempfile
import time
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pandas as pd
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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("SimpleWorkflow/processing.log", mode="a"),
    ],
)
logger = logging.getLogger(__name__)

# Constants
METADATA_PATH = "sql/metadata_table/flora_fauna_metadata_indexed.parquet"
OUTPUT_DIR = Path("SimpleWorkflow/ParsedFiles")
TEMP_DIR = Path(tempfile.gettempdir()) / "pdf_processing"
MAX_RETRIES = 3  # Maximum retries for S3 operations
RETRY_DELAY = 2  # Seconds to wait between retries


@dataclass
class ProcessingStats:
    """Track processing statistics."""

    total: int = 0
    processed: int = 0
    skipped: int = 0
    failed: int = 0
    errors: list[tuple[str, str]] = None

    def __post_init__(self):
        if self.errors is None:
            self.errors = []

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


def verify_naming_convention(df: pd.DataFrame) -> tuple[bool, list[str]]:
    """Verify that existing files match the dataframe index naming convention.

    Args:
        df: Metadata dataframe with index values

    Returns:
        Tuple of (all_valid, list_of_mismatched_files)
    """
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


def save_error_markdown(
    index_value: str,
    error: Exception,
    row: pd.Series,
    s3_key: str = None,
) -> None:
    """Save error details to a markdown file for debugging.

    Args:
        index_value: The index identifier for the file
        error: The exception that occurred
        row: Metadata row from the dataframe
        s3_key: The S3 key if available
    """
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
        logger.info(f"Saved error report: {error_path}")
    except Exception as e:
        logger.error(f"Failed to save error report for {index_value}: {e}")


def process_single_pdf(
    row: pd.Series,
    index_value: str,
    downloader: S3Downloader,
    skip_existing: bool = True,
) -> tuple[bool, str]:
    """Process a single PDF: download, convert to markdown, and save.

    Args:
        row: Metadata row from the dataframe
        index_value: The index identifier for the file
        downloader: S3Downloader instance
        skip_existing: Skip if markdown already exists

    Returns:
        Tuple of (success, status) where status is 'processed', 'skipped', or 'failed'
    """
    # Sanity check: Verify the index matches the row name
    if hasattr(row, "name") and str(row.name) != index_value:
        logger.error(
            f"SANITY CHECK FAILED: Index '{index_value}' does not match row.name '{row.name}'. "
            f"This indicates a serious data integrity issue."
        )
        # This should never happen if the code is correct
        raise ValueError(
            f"Index mismatch: processing '{index_value}' but row has index '{row.name}'"
        )

    # Build output path for markdown (preserve naming convention)
    safe_index = _sanitize_filename_component(index_value)
    markdown_path = OUTPUT_DIR / f"{safe_index}.md"
    error_path = OUTPUT_DIR / f"FAILED-{safe_index}.md"

    # Skip if already exists - check before any download
    if skip_existing and markdown_path.exists():
        logger.debug(f"Skipping existing: {markdown_path}")
        return True, "skipped"

    # Also skip if we already have a failure report for this file
    if skip_existing and error_path.exists():
        logger.debug(f"Skipping previously failed: {error_path}")
        return True, "skipped"

    # Build temporary PDF path
    temp_pdf_path = TEMP_DIR / f"{safe_index}.pdf"
    s3_key = None  # Initialize for error handling

    try:
        # Resolve S3 bucket and key
        bucket, s3_key = _resolve_bucket_and_key(row)

        # Skip macOS system files
        if "__MACOSX" in s3_key or "/._" in s3_key or s3_key.startswith("._"):
            logger.info(f"Skipping macOS system file: {s3_key}")
            return True, "skipped"

        # Check if it's from a compressed file (ZIP)
        from_zip = bool(row.get("from_compressed_file", False))

        if from_zip:
            # Download to memory and extract PDF from ZIP with retry logic
            logger.info(f"Downloading ZIP from s3://{bucket}/{s3_key}")

            content = None
            for attempt in range(MAX_RETRIES):
                try:
                    content = downloader.download_to_memory(bucket, s3_key)
                    break
                except Exception as e:
                    if attempt < MAX_RETRIES - 1:
                        logger.warning(
                            f"Download attempt {attempt + 1} failed, retrying: {e}"
                        )
                        time.sleep(RETRY_DELAY)
                    else:
                        raise

            # Check if it's actually a PDF (mismarked as compressed)
            if _looks_like_pdf(content):
                logger.info(
                    "File marked as compressed but is actually a PDF, treating as direct PDF"
                )
                temp_pdf_path.write_bytes(content)
            else:
                # Try to extract PDF from ZIP
                prefer_name = row.get("file_name")
                internal_name, pdf_bytes = _extract_pdf_from_zip_bytes(
                    content, prefer_name=prefer_name
                )
                logger.info(f"Extracted '{internal_name}' from ZIP")

                # Save PDF bytes to temp file
                temp_pdf_path.write_bytes(pdf_bytes)
        else:
            # Direct PDF download with retry logic
            logger.info(f"Downloading PDF from s3://{bucket}/{s3_key}")

            for attempt in range(MAX_RETRIES):
                try:
                    downloader.download_to_file(bucket, s3_key, temp_pdf_path)
                    break
                except Exception as e:
                    if attempt < MAX_RETRIES - 1:
                        logger.warning(
                            f"Download attempt {attempt + 1} failed, retrying: {e}"
                        )
                        time.sleep(RETRY_DELAY)
                        # Clean up partial download if exists
                        if temp_pdf_path.exists():
                            temp_pdf_path.unlink()
                    else:
                        raise

        # Validate PDF file before processing
        if not temp_pdf_path.exists():
            raise FileNotFoundError(
                f"PDF file not found after download: {temp_pdf_path}"
            )

        file_size_mb = temp_pdf_path.stat().st_size / (1024 * 1024)
        logger.info(f"PDF file size: {file_size_mb:.2f} MB")

        if file_size_mb > 100:  # Warn for large files
            logger.warning(
                f"Large PDF file ({file_size_mb:.2f} MB), processing may take time"
            )

        # Convert PDF to Markdown
        logger.info(f"Converting to markdown: {temp_pdf_path.name}")
        markdown_content, metadata = extract_markdown(
            temp_pdf_path,
            output_dir=None,  # Don't auto-save, we'll handle it
            ignore_images=True,  # Focus on text for RAG
            clean_text=True,
            validate_quality=True,
            show_progress=False,
        )

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
        # Remove surrogate pairs and other problematic characters
        full_markdown = full_markdown.encode("utf-8", errors="ignore").decode(
            "utf-8", errors="ignore"
        )

        # Save markdown file
        markdown_path.write_text(full_markdown, encoding="utf-8")
        logger.info(f"Saved markdown: {markdown_path}")

        return True, "processed"

    except Exception as e:
        logger.error(f"Failed to process {index_value}: {str(e)}")

        # Save error details to markdown file
        save_error_markdown(index_value, e, row, s3_key)

        return False, "failed"

    finally:
        # Clean up temporary PDF
        if temp_pdf_path.exists():
            temp_pdf_path.unlink()
            logger.debug(f"Deleted temp file: {temp_pdf_path}")


def process_batch(
    df: pd.DataFrame,
    indices: Optional[list[str]] = None,
    max_files: Optional[int] = None,
    skip_existing: bool = True,
    dry_run: bool = False,
) -> ProcessingStats:
    """Process a batch of PDFs from the metadata.

    Args:
        df: Metadata dataframe
        indices: Specific indices to process (None for all)
        max_files: Maximum number of files to process
        skip_existing: Skip files that already have markdown
        dry_run: If True, only show what would be processed

    Returns:
        ProcessingStats with results
    """
    stats = ProcessingStats()

    # Determine which indices to process
    if indices:
        process_indices = indices
    else:
        process_indices = list(df.index)

    # Limit if max_files specified
    if max_files:
        process_indices = process_indices[:max_files]

    stats.total = len(process_indices)
    logger.info(f"Processing {stats.total} files...")

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

        # Show sample of what would be processed
        sample_count = 0
        for idx in process_indices:
            if sample_count >= 5:  # Show first 5
                break
            safe_idx = _sanitize_filename_component(idx)
            markdown_path = OUTPUT_DIR / f"{safe_idx}.md"
            error_path = OUTPUT_DIR / f"FAILED-{safe_idx}.md"

            if markdown_path.exists():
                status = "EXISTS"
            elif error_path.exists():
                status = "FAILED"
            else:
                status = "NEW"

            if not (skip_existing and (markdown_path.exists() or error_path.exists())):
                logger.info(f"    {idx} -> {markdown_path.name} [{status}]")
                sample_count += 1

        if would_process > 5:
            logger.info(f"    ... and {would_process - 5} more new files")

        stats.total = len(process_indices)
        stats.skipped = would_skip
        return stats

    # Initialize S3 downloader
    config = S3Config.from_env()
    downloader = S3Downloader(config)

    # Process files with progress bar
    with tqdm(total=stats.total, desc="Processing PDFs") as pbar:
        for idx in process_indices:
            try:
                # Process the PDF (the function now handles the existence check)
                row = df.loc[idx]
                success, status = process_single_pdf(
                    row, idx, downloader, skip_existing=skip_existing
                )

                if status == "skipped":
                    stats.skipped += 1
                    pbar.set_postfix({"skipped": stats.skipped})
                elif status == "processed":
                    stats.processed += 1
                    pbar.set_postfix({"processed": stats.processed})
                elif status == "failed":
                    stats.failed += 1
                    stats.errors.append((idx, "Processing failed"))
                    pbar.set_postfix({"failed": stats.failed})

            except Exception as e:
                stats.failed += 1
                stats.errors.append((idx, str(e)))
                logger.error(f"Error processing {idx}: {e}")
                pbar.set_postfix({"failed": stats.failed})

            pbar.update(1)

    return stats


def main():
    """Main execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert PDFs from S3 to Markdown using metadata"
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

    args = parser.parse_args()

    # Ensure directories exist
    ensure_directories()

    # Load metadata
    logger.info(f"Loading metadata from {METADATA_PATH}")
    try:
        df = pd.read_parquet(METADATA_PATH)
        logger.info(f"Loaded {len(df)} records")
    except Exception as e:
        logger.error(f"Failed to load metadata: {e}")
        sys.exit(1)

    # Verify naming convention sanity check
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

    # Process files
    stats = process_batch(
        df,
        indices=args.indices,
        max_files=args.max_files,
        skip_existing=args.skip_existing,
        dry_run=args.dry_run,
    )

    # Log summary
    stats.log_summary()

    # Clean up temp directory if empty
    if TEMP_DIR.exists() and not any(TEMP_DIR.iterdir()):
        TEMP_DIR.rmdir()
        logger.info("Cleaned up empty temp directory")

    return 0 if stats.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
