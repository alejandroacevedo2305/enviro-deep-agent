"""Utilities to validate metadata and set index from ``file_identifier``.

This module reads a Parquet metadata table and replaces the DataFrame index
with the string from the ``file_identifier`` column.

uv run -m sql.validate_available_metadata
"""

# %%
import sys
from pathlib import Path

import pandas as pd

# Add parent directory to path to import from SimpleWorkflow
sys.path.insert(0, str(Path(__file__).parent.parent))
from SimpleWorkflow.summarize_markdown_outputs import summarize_markdown_outputs


def set_file_identifier_index(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of ``df`` indexed by the ``file_identifier`` column.

    The resulting index is named ``file_identifier``. Values are cast to pandas'
    nullable string dtype and missing values are treated as empty strings.
    """
    if "file_identifier" not in df.columns:
        raise KeyError("Missing required column to build index: file_identifier")

    df_with_index = df.copy()
    index_series = df_with_index["file_identifier"].astype("string").fillna("")
    df_with_index.index = index_series
    df_with_index.index.name = "file_identifier"
    return df_with_index


def set_composite_index(df: pd.DataFrame) -> pd.DataFrame:
    """Deprecated: use ``set_file_identifier_index`` instead."""
    return set_file_identifier_index(df)


def save_indexed_metadata(df: pd.DataFrame) -> None:
    """Save the indexed metadata to a Parquet file."""
    df.to_parquet(
        "sql/metadata_table/flora_fauna_metadata_indexed.parquet",
        index=True,
        compression="gzip",
    )


def load_indexed_metadata() -> pd.DataFrame:
    """Load the indexed metadata from a Parquet file."""
    return pd.read_parquet("sql/metadata_table/flora_fauna_metadata_indexed.parquet")


def print_line_count_distribution(summary: dict) -> None:
    """Print distribution of files by line count ranges.

    Excludes FAILED- files and reports failure percentage separately.
    """
    if not summary:
        print("No file statistics available")
        return

    total_files = summary.get("total_files", 0)
    success_files = summary.get("success_files", 0)
    failed_files = summary.get("failed_files", 0)

    if total_files == 0:
        print("No files found")
        return

    # Calculate failure percentage
    failure_rate = (failed_files / total_files) * 100 if total_files > 0 else 0

    # Print failure statistics
    print("\n" + "=" * 70)
    print("FILE PROCESSING SUMMARY")
    print("=" * 70)
    print(f"Total files:        {total_files:>10,}")
    print(f"✓ Successful:       {success_files:>10,}")
    print(f"✗ Failed (FAILED-): {failed_files:>10,}")
    print(f"Failure rate:       {failure_rate:>10.2f}%")
    print("=" * 70)

    # Only process successful files for line count distribution
    file_details = summary.get("file_details", [])
    if not file_details:
        print("\nNo successful file statistics available")
        return

    # Define ranges
    ranges = [
        (5000, float("inf"), "more than 5,000 lines"),
        (1000, 5000, "less than 5,000 and more than 1,000 lines"),
        (100, 1000, "less than 1,000 and more than 100 lines"),
        (10, 100, "less than 100 and more than 10 lines"),
        (1, 10, "less than 10 and more than 1 lines"),
    ]

    print("\n" + "=" * 70)
    print("LINE COUNT DISTRIBUTION (Successful files only)")
    print("=" * 70)

    for min_val, max_val, label in ranges:
        if max_val == float("inf"):
            count = sum(1 for f in file_details if f["lines"] >= min_val)
        else:
            count = sum(1 for f in file_details if min_val < f["lines"] <= max_val)
        print(f"Files with {label}: {count:>5,}")

    print("=" * 70 + "\n")


if __name__ == "__main__":
    # Simple demonstration / validation
    PARQUET_PATH = "sql/metadata_table/flora_fauna_metadata.parquet"
    df_original = pd.read_parquet(PARQUET_PATH)
    print("original shape:", df_original.shape)

    df_indexed = set_file_identifier_index(df_original)
    print("indexed shape:", df_indexed.shape)
    print("index name:", df_indexed.index.name)

    # Quick sanity checks
    assert len(df_indexed) == len(df_original)
    print(
        "sample index keys:\n",
        df_indexed.index.to_series().head().to_string(index=False),
    )

    save_indexed_metadata(df_indexed)
    df_indexed_loaded = load_indexed_metadata()
    print("indexed shape:", df_indexed_loaded.shape)
    print("index name:", df_indexed_loaded.index.name)

    # Quick sanity checks
    assert len(df_indexed_loaded) == len(df_indexed)
    print(
        "sample index keys:\n",
        df_indexed_loaded.index.to_series().head().to_string(index=False),
    )
    print(f"Column names: {df_indexed_loaded.columns}")

    # Analyze markdown files and print line count distribution
    markdown_dir = Path("SimpleWorkflow/ParsedFiles")
    if markdown_dir.exists():
        summary = summarize_markdown_outputs(markdown_dir)
        print_line_count_distribution(summary)
    else:
        print(f"\nMarkdown directory not found: {markdown_dir}")

# %%
