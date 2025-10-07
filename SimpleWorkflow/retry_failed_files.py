"""Retry failed files.

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

Run it using uv:
    uv run -m SimpleWorkflow.retry_failed_files

Or directly:
    uv run python SimpleWorkflow/retry_failed_files.py

Features:
- Async S3 downloads for efficiency
- Process pool for CPU-bound markdown extraction
- Detailed progress tracking with success/failure counts
- Automatic cleanup of successful retries
- Handles UTF-8 BOM automatically
"""

# %%
from __future__ import annotations

import asyncio
import logging
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Optional

import aioboto3
import pandas as pd
from dotenv import load_dotenv

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
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Constants
OUTPUT_DIR = Path("SimpleWorkflow/ParsedFiles")
PARQUET_PATH = "sql/metadata_table/flora_fauna_metadata_indexed.parquet"
MAX_WORKERS = 4


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
    except Exception as e:
        logger.error(f"Failed to parse {failed_file_path}: {e}")
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
                f"Found failed file: {metadata['file_identifier']} "
                f"(error: {metadata.get('error', 'unknown')})"
            )
        else:
            logger.warning(f"Could not parse metadata from {failed_path}")

    return failed_files


async def download_from_s3_async(
    session,
    bucket: str,
    s3_key: str,
) -> bytes:
    """Download file from S3 asynchronously.

    Args:
        session: aioboto3 session
        bucket: S3 bucket name
        s3_key: S3 object key

    Returns:
        File content as bytes
    """
    async with session.client("s3") as s3_client:
        response = await s3_client.get_object(Bucket=bucket, Key=s3_key)
        async with response["Body"] as stream:
            return await stream.read()


def extract_markdown_worker(pdf_path_str: str) -> tuple[str, any]:
    """Worker function for PDF extraction (must be picklable).

    Args:
        pdf_path_str: Path to PDF file as string

    Returns:
        Tuple of (markdown_content, error_or_None)
    """
    try:
        # extract_markdown returns (markdown_text, metadata)
        markdown_text, metadata = extract_markdown(pdf_path_str)
        return markdown_text, None
    except Exception as e:
        logger.error(f"Markdown extraction failed for {pdf_path_str}: {e}")
        return "", e


async def process_pdf_async(
    pdf_bytes: bytes,
    file_identifier: str,
    executor: ProcessPoolExecutor,
) -> tuple[bool, str, Optional[str]]:
    """Process PDF bytes to markdown asynchronously.

    Args:
        pdf_bytes: PDF content as bytes
        file_identifier: Unique identifier for the file
        executor: ProcessPoolExecutor for CPU-bound markdown extraction

    Returns:
        Tuple of (success, markdown_content, error_message)
    """
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

        return True, markdown, None

    except Exception as e:
        logger.error(f"PDF processing failed for {file_identifier}: {e}")
        return False, "", str(e)
    finally:
        # Clean up temp file
        if temp_pdf_path.exists():
            try:
                temp_pdf_path.unlink()
            except Exception as e:
                logger.warning(f"Failed to delete temp file {temp_pdf_path}: {e}")


async def retry_single_file(
    session,
    failed_path: Path,
    metadata: dict,
    df_metadata: pd.DataFrame,
    executor: ProcessPoolExecutor,
) -> bool:
    """Retry processing a single failed file.

    Args:
        session: aioboto3 session
        failed_path: Path to the FAILED-*.md file
        metadata: Parsed metadata from the failed file
        df_metadata: Full metadata DataFrame
        executor: ProcessPoolExecutor for markdown extraction

    Returns:
        True if successful, False otherwise
    """
    file_identifier = metadata["file_identifier"]
    s3_key = metadata["s3_key"]

    try:
        # Try to get additional info from metadata DataFrame
        print("    ⤷ Resolving S3 location...")
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
                if not s3_key.startswith("sea-crawler/"):
                    s3_key = s3_key

        # Download from S3 (treating as direct PDF, not ZIP)
        print(f"    ⤷ Downloading from S3 (bucket: {bucket})...")
        pdf_bytes = await download_from_s3_async(session, bucket, s3_key)
        size_mb = len(pdf_bytes) / (1024 * 1024)
        print(f"    ⤷ Downloaded {size_mb:.2f} MB")

        # Check for empty files
        if len(pdf_bytes) == 0:
            print("    ⤷ ERROR: Empty file (0 bytes)")
            return False

        # Remove UTF-8 BOM if present (some files have this)
        if pdf_bytes.startswith(b"\xef\xbb\xbf"):
            print("    ⤷ Detected UTF-8 BOM, removing...")
            pdf_bytes = pdf_bytes[3:]

        # Verify it's actually a PDF
        if not pdf_bytes.startswith(b"%PDF"):
            print(f"    ⤷ ERROR: Not a PDF file (starts with: {pdf_bytes[:20]!r})")
            return False

        print("    ⤷ Verified PDF format")

        # Process PDF to markdown
        print(f"    ⤷ Extracting markdown (using {MAX_WORKERS} workers)...")
        success, markdown_content, error_msg = await process_pdf_async(
            pdf_bytes, file_identifier, executor
        )

        if not success:
            print(f"    ⤷ ERROR: Markdown extraction failed: {error_msg}")
            return False

        # Save successful result
        output_path = OUTPUT_DIR / f"{file_identifier}.md"
        output_path.write_text(markdown_content, encoding="utf-8")
        lines = len(markdown_content.split("\n"))
        size_kb = len(markdown_content) / 1024
        print(f"    ⤷ Saved markdown: {size_kb:.1f} KB, {lines} lines")

        # Remove the FAILED file
        failed_path.unlink()
        print("    ⤷ Cleaned up failed marker file")

        return True

    except Exception as e:
        print(f"    ⤷ ERROR: {type(e).__name__}: {e}")
        logger.debug(f"Full error for {file_identifier}:", exc_info=True)
        return False


async def retry_all_failed_files():
    """Main async function to retry all failed files."""
    # Find all failed files
    print("\n" + "=" * 70)
    print("FAILED FILES RETRY PROCESS")
    print("=" * 70 + "\n")

    failed_files = find_failed_files()

    if not failed_files:
        logger.info("No failed files found to retry.")
        return

    total_files = len(failed_files)
    print(f"\n📊 Summary: Found {total_files} failed files to retry\n")

    # Load metadata
    try:
        print("📖 Loading metadata...")
        df_metadata = load_metadata(PARQUET_PATH)
        logger.info(f"✓ Loaded metadata with {len(df_metadata)} rows")
    except Exception as e:
        logger.error(f"✗ Failed to load metadata: {e}")
        return

    # Create async S3 session
    s3_config = S3Config.from_env()
    session_kwargs = {}
    if s3_config.region_name:
        session_kwargs["region_name"] = s3_config.region_name

    session = aioboto3.Session(**session_kwargs)

    # Create process pool for CPU-bound markdown extraction
    executor = ProcessPoolExecutor(max_workers=MAX_WORKERS)

    try:
        success_count = 0
        fail_count = 0

        print(f"\n🔄 Starting retry process ({MAX_WORKERS} workers)...\n")
        print("-" * 70)

        for idx, (failed_path, metadata) in enumerate(failed_files, 1):
            file_id = metadata["file_identifier"]
            progress_pct = (idx / total_files) * 100

            print(
                f"\n[{idx}/{total_files}] ({progress_pct:.1f}%) Processing: {file_id}"
            )
            print(f"    Error was: {metadata.get('error', 'unknown')}")

            success = await retry_single_file(
                session, failed_path, metadata, df_metadata, executor
            )

            if success:
                success_count += 1
                print("    ✓ SUCCESS - Parsed and saved")
            else:
                fail_count += 1
                print("    ✗ FAILED - Still unable to process")

            # Progress summary
            print(
                f"    Progress: ✓ {success_count} succeeded | "
                f"✗ {fail_count} failed | "
                f"⏳ {total_files - idx} remaining"
            )

        print("\n" + "=" * 70)
        print("RETRY PROCESS COMPLETED")
        print("=" * 70)
        print("\n📈 Final Results:")
        print(f"   ✓ Successful: {success_count}/{total_files}")
        print(f"   ✗ Failed:     {fail_count}/{total_files}")
        print(
            f"   Success Rate: "
            f"{(success_count / total_files * 100) if total_files > 0 else 0:.1f}%"
        )
        print()

    finally:
        executor.shutdown(wait=True)


def main():
    """Main entry point."""
    logger.info("Starting failed file retry process...")
    asyncio.run(retry_all_failed_files())
    logger.info("Done.")


if __name__ == "__main__":
    main()
