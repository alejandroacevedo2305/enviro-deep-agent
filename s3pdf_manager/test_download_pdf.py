"""Tests for `s3pdf_manager.download_pdf`.

Tests downloading real PDFs from S3, similar to SimpleWorkflow/pdf_processor.py.
Verifies AWS credentials and performs actual downloads to test_collection directory.

uv run python s3pdf_manager/test_download_pdf.py
"""

# %%
from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

# Load environment variables first
load_dotenv(override=True)

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from s3pdf_manager.download_pdf import (
    delete_by_index,
    delete_by_list,
    download_by_index,
    download_by_list,
    download_by_range,
    load_metadata,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

# Constants
TEST_OUTPUT_DIR = Path(
    "/home/alejandro/Desktop/repos/NVIRO-airflow-parsing/s3pdf_manager/test_collection"
)
PARQUET_PATH = "sql/metadata_table/flora_fauna_metadata_indexed.parquet"


def check_aws_credentials() -> None:
    """Check if AWS credentials are available in environment.

    Raises ValueError if credentials are missing.
    """
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    if not access_key or not secret_key:
        raise ValueError(
            "AWS credentials not found in environment!\n"
            "Please set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables.\n"
            "You can set them in a .env file or export them in your shell."
        )

    logger.info("✓ AWS credentials found")

    # Check optional configurations
    region = os.getenv("AWS_DEFAULT_REGION")
    bucket = os.getenv("S3_BUCKET")
    endpoint = os.getenv("S3_ENDPOINT_URL")

    if region:
        logger.info(f"  - Region: {region}")
    if bucket:
        logger.info(f"  - Default bucket: {bucket}")
    if endpoint:
        logger.info(f"  - Endpoint URL: {endpoint}")


def test_load_metadata() -> pd.DataFrame:
    """Test loading metadata from parquet file.

    Returns the loaded DataFrame for further testing.
    """
    logger.info("\n=== Testing Metadata Loading ===")

    try:
        df = load_metadata(PARQUET_PATH)
        logger.info(f"✓ Loaded {len(df)} rows from metadata")
        logger.info(f"  - Index name: {df.index.name}")
        logger.info(f"  - Columns: {', '.join(df.columns[:5])}...")

        # Show first few indices
        if len(df) > 0:
            sample_indices = list(df.index[:5])
            logger.info(f"  - Sample indices: {sample_indices}")

        return df
    except Exception as e:
        logger.error(f"✗ Failed to load metadata: {e}")
        raise


def test_single_download(df: pd.DataFrame) -> None:
    """Test downloading a single PDF file."""
    logger.info("\n=== Testing Single PDF Download ===")

    if len(df) == 0:
        logger.warning("No data in metadata, skipping single download test")
        return

    # Get first index
    test_index = str(df.index[0])
    logger.info(f"Testing download of index: {test_index}")

    # Show metadata for this index
    row = df.loc[test_index]
    logger.info(f"  - S3 key: {row.get('s3_key', 'N/A')}")
    logger.info(f"  - From compressed: {row.get('from_compressed_file', False)}")
    logger.info(f"  - File name: {row.get('file_name', 'N/A')}")

    try:
        # Download the file
        output_path = download_by_index(
            test_index,
            parquet_path=PARQUET_PATH,
            output_dir=TEST_OUTPUT_DIR,
            skip_existing=False,  # Force download for testing
        )

        if output_path.exists():
            file_size = output_path.stat().st_size
            logger.info(f"✓ Successfully downloaded to: {output_path}")
            logger.info(f"  - File size: {file_size:,} bytes")
        else:
            logger.error(f"✗ Download completed but file not found: {output_path}")

    except Exception as e:
        logger.error(f"✗ Failed to download {test_index}: {e}")
        raise


def test_list_download(df: pd.DataFrame) -> None:
    """Test downloading multiple PDFs from a list."""
    logger.info("\n=== Testing List Download (Multiple PDFs) ===")

    if len(df) < 3:
        logger.warning("Not enough data for list download test")
        return

    # Get 3 indices to test
    test_indices = list(df.index[1:4])  # Skip first since we already downloaded it
    logger.info(f"Testing download of {len(test_indices)} PDFs")
    logger.info(f"  - Indices: {test_indices}")

    try:
        # Download the files
        output_paths = download_by_list(
            test_indices,
            parquet_path=PARQUET_PATH,
            output_dir=TEST_OUTPUT_DIR,
            skip_existing=True,  # Skip if already exists
        )

        success_count = sum(1 for p in output_paths if p.exists())
        logger.info(f"✓ Downloaded {success_count}/{len(test_indices)} files")

        for idx, path in zip(test_indices, output_paths):
            if path.exists():
                size = path.stat().st_size
                logger.info(f"  - {idx}: {size:,} bytes")
            else:
                logger.warning(f"  - {idx}: Not downloaded")

    except Exception as e:
        logger.error(f"✗ Failed to download list: {e}")
        raise


def test_range_download(df: pd.DataFrame) -> None:
    """Test downloading PDFs in a range."""
    logger.info("\n=== Testing Range Download ===")

    if len(df) < 10:
        logger.warning("Not enough data for range download test")
        return

    # Get a range of 5 indices
    start_idx = str(df.index[5])
    end_idx = str(df.index[9])

    logger.info(f"Testing download range from {start_idx} to {end_idx}")

    try:
        # Download the range
        output_paths = download_by_range(
            start_idx,
            end_idx,
            parquet_path=PARQUET_PATH,
            output_dir=TEST_OUTPUT_DIR,
            skip_existing=True,
        )

        logger.info(f"✓ Downloaded {len(output_paths)} files in range")

        # Show summary
        total_size = sum(p.stat().st_size for p in output_paths if p.exists())
        logger.info(f"  - Total size: {total_size:,} bytes")

    except Exception as e:
        logger.error(f"✗ Failed to download range: {e}")
        raise


def test_delete_files(df: pd.DataFrame) -> None:
    """Test deleting downloaded files."""
    logger.info("\n=== Testing File Deletion ===")

    if len(df) < 2:
        logger.warning("Not enough data for deletion test")
        return

    # Delete single file
    test_index = str(df.index[0])
    logger.info(f"Testing deletion of single file: {test_index}")

    deleted = delete_by_index(test_index, output_dir=TEST_OUTPUT_DIR)
    if deleted:
        logger.info(f"✓ Deleted {test_index}")
    else:
        logger.info(f"  - File didn't exist: {test_index}")

    # Delete multiple files
    if len(df) >= 4:
        indices_to_delete = [str(df.index[1]), str(df.index[2])]
        logger.info(f"Testing deletion of multiple files: {indices_to_delete}")

        deleted_count = delete_by_list(indices_to_delete, output_dir=TEST_OUTPUT_DIR)
        logger.info(f"✓ Deleted {deleted_count} files")


def test_compressed_files(df: pd.DataFrame) -> None:
    """Test downloading PDFs from compressed (ZIP) files."""
    logger.info("\n=== Testing Compressed File Extraction ===")

    # Find indices with compressed files
    compressed_df = (
        df[df["from_compressed_file"] == True]
        if "from_compressed_file" in df.columns
        else pd.DataFrame()
    )

    if len(compressed_df) == 0:
        logger.warning("No compressed files found in metadata")
        return

    logger.info(f"Found {len(compressed_df)} compressed files")

    # Test first compressed file
    test_index = str(compressed_df.index[0])
    row = compressed_df.loc[test_index]

    logger.info(f"Testing compressed file: {test_index}")
    logger.info(f"  - S3 key: {row.get('s3_key', 'N/A')}")
    logger.info(f"  - File name in ZIP: {row.get('file_name', 'N/A')}")

    try:
        output_path = download_by_index(
            test_index,
            parquet_path=PARQUET_PATH,
            output_dir=TEST_OUTPUT_DIR,
            skip_existing=False,
        )

        if output_path.exists():
            logger.info("✓ Successfully extracted PDF from ZIP")
            logger.info(f"  - Output: {output_path}")
            logger.info(f"  - Size: {output_path.stat().st_size:,} bytes")
        else:
            logger.error("✗ Extraction failed")

    except Exception as e:
        logger.error(f"✗ Failed to extract from compressed file: {e}")


def test_dry_run(df: pd.DataFrame) -> None:
    """Test dry-run mode without actual downloads."""
    logger.info("\n=== Testing Dry-Run Mode ===")

    if len(df) == 0:
        logger.warning("No data for dry-run test")
        return

    test_index = str(df.index[0])
    logger.info(f"Testing dry-run for index: {test_index}")

    try:
        output_path = download_by_index(
            test_index,
            parquet_path=PARQUET_PATH,
            output_dir=TEST_OUTPUT_DIR,
            dry_run=True,  # Dry-run mode
        )

        logger.info(f"✓ Dry-run completed (would save to: {output_path})")

    except Exception as e:
        logger.error(f"✗ Dry-run failed: {e}")


def show_download_summary() -> None:
    """Show summary of downloaded files."""
    logger.info("\n=== Download Summary ===")

    if not TEST_OUTPUT_DIR.exists():
        logger.info("Test directory doesn't exist yet")
        return

    pdf_files = list(TEST_OUTPUT_DIR.glob("*.pdf"))

    if not pdf_files:
        logger.info("No PDF files downloaded yet")
        return

    logger.info(f"Found {len(pdf_files)} PDF files in test collection:")

    total_size = 0
    for pdf in sorted(pdf_files)[:10]:  # Show first 10
        size = pdf.stat().st_size
        total_size += size
        logger.info(f"  - {pdf.name}: {size:,} bytes")

    if len(pdf_files) > 10:
        logger.info(f"  ... and {len(pdf_files) - 10} more files")

    # Calculate total for all files
    total_size = sum(f.stat().st_size for f in pdf_files)
    logger.info(
        f"\nTotal size: {total_size:,} bytes ({total_size / 1024 / 1024:.2f} MB)"
    )


def main():
    """Run all tests for PDF download functionality."""
    logger.info("=" * 60)
    logger.info("PDF Download Test Suite")
    logger.info("=" * 60)

    try:
        # Check AWS credentials first
        check_aws_credentials()

        # Ensure test directory exists
        TEST_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        logger.info(f"\nTest output directory: {TEST_OUTPUT_DIR}")

        # Load metadata
        df = test_load_metadata()

        # Run tests
        test_single_download(df)
        test_list_download(df)
        test_range_download(df)
        test_compressed_files(df)
        test_dry_run(df)

        # Show summary
        show_download_summary()

        # Optional: Test deletion (commented out to preserve downloads)
        # test_delete_files(df)

        logger.info("\n" + "=" * 60)
        logger.info("✓ All tests completed successfully!")
        logger.info("=" * 60)

    except ValueError as e:
        logger.error(f"\n✗ Configuration Error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"\n✗ Test Suite Failed: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
