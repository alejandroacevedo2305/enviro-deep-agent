"""Convert markdown files to LangChain Documents with metadata.

This script reads markdown files from ParsedFiles/, matches them with metadata
from flora_fauna_metadata_indexed.parquet, and saves them as LangChain
Document objects in JSON format for vector store upload.

Usage:
    uv run python PrepareDocsForUpsert/OneToOneDocs/md_to_doc.py
"""

# %%
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from langchain_core.documents import Document


def load_metadata_table(parquet_path: Path) -> pd.DataFrame:
    """Load the parquet file with metadata indexed by file_identifier.

    Args:
        parquet_path: Path to the parquet file

    Returns:
        DataFrame indexed by file_identifier
    """
    df = pd.read_parquet(parquet_path)
    print(f"Loaded {len(df)} metadata records from {parquet_path}")
    return df


def get_markdown_files(markdown_dir: Path, exclude_failed: bool = True) -> list[Path]:
    """Get all markdown files from the directory.

    Args:
        markdown_dir: Directory containing markdown files
        exclude_failed: If True, exclude files starting with "FAILED-"

    Returns:
        List of Path objects for markdown files
    """
    all_md_files = list(markdown_dir.glob("*.md"))

    if exclude_failed:
        md_files = [f for f in all_md_files if not f.name.startswith("FAILED-")]
        print(
            f"Found {len(all_md_files)} markdown files, "
            f"{len(md_files)} non-failed files"
        )
    else:
        md_files = all_md_files
        print(f"Found {len(md_files)} markdown files")

    return md_files


def extract_file_identifier(md_path: Path) -> str:
    """Extract file_identifier from markdown filename.

    Args:
        md_path: Path to markdown file

    Returns:
        File identifier (filename without .md extension)
    """
    return md_path.stem


def create_document_from_markdown(
    md_path: Path, metadata_dict: dict[str, Any]
) -> Document:
    """Create a LangChain Document from markdown file and metadata.

    Args:
        md_path: Path to markdown file
        metadata_dict: Dictionary containing metadata for the document

    Returns:
        LangChain Document object
    """
    # Read markdown content
    page_content = md_path.read_text(encoding="utf-8")

    # Create Document with page_content and metadata
    doc = Document(page_content=page_content, metadata=metadata_dict)

    return doc


def convert_numpy_to_native(obj: Any) -> Any:
    """Convert numpy types to native Python types for JSON serialization.

    Args:
        obj: Object that may contain numpy types

    Returns:
        Object with numpy types converted to native Python types
    """
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, dict):
        return {key: convert_numpy_to_native(value) for key, value in (obj.items())}
    if isinstance(obj, (list, tuple)):
        return [convert_numpy_to_native(item) for item in obj]
    return obj


def save_document_as_json(doc: Document, output_path: Path) -> None:
    """Save a LangChain Document as JSON file.

    Args:
        doc: LangChain Document object
        output_path: Path where to save the JSON file
    """
    # Convert metadata to ensure no numpy types
    metadata_clean = convert_numpy_to_native(doc.metadata)

    doc_dict = {"page_content": doc.page_content, "metadata": metadata_clean}

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(doc_dict, f, ensure_ascii=False, indent=2)


def process_markdown_to_documents(
    markdown_dir: Path,
    metadata_df: pd.DataFrame,
    output_dir: Path,
    exclude_failed: bool = True,
) -> tuple[int, int, int]:
    """Process all markdown files and convert them to Documents.

    Args:
        markdown_dir: Directory containing markdown files
        metadata_df: DataFrame with metadata indexed by file_identifier
        output_dir: Directory where to save the Document JSON files
        exclude_failed: If True, exclude files starting with "FAILED-"

    Returns:
        Tuple of (successful_count, missing_metadata_count, total_files)
    """
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get all markdown files
    md_files = get_markdown_files(markdown_dir, exclude_failed=exclude_failed)

    successful_count = 0
    missing_metadata_count = 0

    for md_path in md_files:
        file_identifier = extract_file_identifier(md_path)

        # Check if metadata exists for this file
        if file_identifier not in metadata_df.index:
            print(f"WARNING: No metadata found for {file_identifier}, skipping...")
            missing_metadata_count += 1
            continue

        # Get metadata from dataframe
        metadata_row = metadata_df.loc[file_identifier]

        # Use metadata_with_classes as the metadata
        metadata_dict = metadata_row["metadata_with_classes"]

        # Ensure metadata is a dictionary
        if not isinstance(metadata_dict, dict):
            print(
                f"WARNING: metadata_with_classes is not a dict for "
                f"{file_identifier}, skipping..."
            )
            missing_metadata_count += 1
            continue

        # Create Document
        doc = create_document_from_markdown(md_path, metadata_dict)

        # Save Document as JSON
        output_path = output_dir / f"{file_identifier}.json"
        save_document_as_json(doc, output_path)

        successful_count += 1

        if successful_count % 100 == 0:
            print(f"Processed {successful_count} documents...")

    return successful_count, missing_metadata_count, len(md_files)


def validate_documents(output_dir: Path, num_samples: int = 5) -> bool:
    """Validate generated documents by checking structure and content.

    Args:
        output_dir: Directory containing the generated document JSON files
        num_samples: Number of random samples to validate

    Returns:
        True if validation passes, False otherwise
    """
    import random

    print("\n" + "=" * 80)
    print("VALIDATING DOCUMENTS")
    print("=" * 80)

    json_files = list(output_dir.glob("*.json"))
    if not json_files:
        print("ERROR: No JSON files found in output directory")
        return False

    # Sample random files
    sample_files = random.sample(json_files, min(num_samples, len(json_files)))

    all_valid = True
    for json_file in sample_files:
        try:
            with json_file.open("r", encoding="utf-8") as f:
                doc = json.load(f)

            # Check required keys
            if "page_content" not in doc or "metadata" not in doc:
                print(f"ERROR: Missing required keys in {json_file.name}")
                all_valid = False
                continue

            # Check page_content is non-empty
            if not doc["page_content"] or len(doc["page_content"]) < 100:
                print(
                    f"ERROR: page_content too short in {json_file.name}: "
                    f"{len(doc['page_content'])} chars"
                )
                all_valid = False
                continue

            # Check metadata has required fields
            required_metadata_fields = [
                "fileIdentifier",
                "seaProjectName",
                "classes",
            ]
            for field in required_metadata_fields:
                if field not in doc["metadata"]:
                    print(
                        f"ERROR: Missing metadata field '{field}' in {json_file.name}"
                    )
                    all_valid = False
                    continue

            # Check classes is a list
            if not isinstance(doc["metadata"]["classes"], list):
                print(f"ERROR: 'classes' is not a list in {json_file.name}")
                all_valid = False
                continue

            print(
                f"✓ {json_file.name}: "
                f"{len(doc['page_content'])} chars, "
                f"{len(doc['metadata']['classes'])} classes"
            )

        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {json_file.name}: {e}")
            all_valid = False
        except (KeyError, TypeError, ValueError) as e:
            print(f"ERROR: Unexpected error validating {json_file.name}: {e}")
            all_valid = False

    print()
    if all_valid:
        print("✓ All sampled documents are valid!")
    else:
        print("✗ Some documents failed validation")

    return all_valid


def main() -> None:
    """Main function to orchestrate the conversion process."""
    # Define paths
    base_dir = Path(__file__).parent.parent.parent
    parquet_path = (
        base_dir / "sql" / "metadata_table" / ("flora_fauna_metadata_indexed.parquet")
    )
    markdown_dir = base_dir / "SimpleWorkflow" / "ParsedFiles"
    output_dir = (
        base_dir / "PrepareDocsForUpsert" / "OneToOneDocs" / ("documents_to_upsert")
    )

    print("=" * 80)
    print("Converting Markdown Files to LangChain Documents")
    print("=" * 80)
    print(f"\nMetadata source: {parquet_path}")
    print(f"Markdown source: {markdown_dir}")
    print(f"Output directory: {output_dir}")
    print()

    # Load metadata
    metadata_df = load_metadata_table(parquet_path)

    # Process markdown files
    successful, missing, total = process_markdown_to_documents(
        markdown_dir=markdown_dir,
        metadata_df=metadata_df,
        output_dir=output_dir,
        exclude_failed=True,
    )

    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total markdown files found: {total}")
    print(f"Successfully converted: {successful}")
    print(f"Missing metadata: {missing}")
    print(f"Success rate: {successful / total * 100:.1f}%")
    print(f"\nDocuments saved to: {output_dir}")
    print("=" * 80)

    # Validate documents
    validation_passed = validate_documents(output_dir, num_samples=10)

    if validation_passed:
        print("\n✓ All documents are ready for vector store upload!")
    else:
        print(
            "\n✗ Some documents may have issues. Please review the validation output."
        )


if __name__ == "__main__":
    main()
