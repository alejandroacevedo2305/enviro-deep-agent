"""Script to populate the Neo4j knowledge graph with documents.

This script loads documents from the documents_to_upsert directory
and populates the Neo4j knowledge graph with proper nodes and relationships.

uv run python Neo4j/upsert/add_documents.py

"""

# %%
from __future__ import annotations

import logging
import sys
from pathlib import Path

# Add parent directories to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from Neo4j.create.KnowledgeGraphDB import KnowledgeGraphDB
from PrepareDocsForUpsert.OneToOneDocs.load_documents import (
    load_all_documents,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def print_unique_metadata_values(documents: list) -> dict[str, set]:
    """Extract and print unique values from document metadata.

    Args:
        documents: List of Document objects

    Returns:
        Dictionary with unique values for each metadata field
    """
    unique_values = {
        "classes": set(),
        "regions": set(),
        "communes": set(),
        "project_types": set(),
        "typologies": set(),
        "projects": set(),
    }

    for doc in documents:
        metadata = doc.metadata

        # Extract classes
        classes = metadata.get("classes", [])
        for class_info in classes:
            if isinstance(class_info, dict):
                class_name = class_info.get("class", "")
                if class_name:
                    unique_values["classes"].add(class_name)

        # Extract other metadata
        if region := metadata.get("seaProjectRegion"):
            unique_values["regions"].add(region)

        if commune := metadata.get("seaProjectEiDocumentCommunes"):
            unique_values["communes"].add(commune)

        if project_type := metadata.get("seaProjectProjectType"):
            unique_values["project_types"].add(project_type)

        if typology := metadata.get("seaProjectTypology"):
            unique_values["typologies"].add(typology)

        if project := metadata.get("seaProjectName"):
            unique_values["projects"].add(project)

    # Print summary
    print("\n" + "=" * 80)
    print("Unique Metadata Values Found")
    print("=" * 80)

    print(f"\nClasses ({len(unique_values['classes'])}):")
    for cls in sorted(unique_values["classes"])[:10]:  # Show first 10
        print(f"  - {cls}")
    if len(unique_values["classes"]) > 10:
        print(f"  ... and {len(unique_values['classes']) - 10} more")

    print(f"\nRegions ({len(unique_values['regions'])}):")
    for region in sorted(unique_values["regions"])[:5]:
        print(f"  - {region}")
    if len(unique_values["regions"]) > 5:
        print(f"  ... and {len(unique_values['regions']) - 5} more")

    print(f"\nCommunes ({len(unique_values['communes'])}):")
    for commune in sorted(unique_values["communes"])[:10]:
        print(f"  - {commune}")
    if len(unique_values["communes"]) > 10:
        print(f"  ... and {len(unique_values['communes']) - 10} more")

    print(f"\nProject Types ({len(unique_values['project_types'])}):")
    for pt in sorted(unique_values["project_types"])[:10]:
        print(f"  - {pt}")
    if len(unique_values["project_types"]) > 10:
        print(f"  ... and {len(unique_values['project_types']) - 10} more")

    print(f"\nTypologies ({len(unique_values['typologies'])}):")
    for typ in sorted(unique_values["typologies"])[:10]:
        print(f"  - {typ}")
    if len(unique_values["typologies"]) > 10:
        print(f"  ... and {len(unique_values['typologies']) - 10} more")

    print(f"\nProjects ({len(unique_values['projects'])}):")
    for proj in sorted(unique_values["projects"])[:5]:
        print(f"  - {proj[:80]}...")  # Truncate long names
    if len(unique_values["projects"]) > 5:
        print(f"  ... and {len(unique_values['projects']) - 5} more")

    return unique_values


def populate_knowledge_graph(
    documents_dir: Path | None = None,
    batch_size: int = 50,
    clear_existing: bool = False,
) -> None:
    """Populate the Neo4j knowledge graph with documents.

    Args:
        documents_dir: Directory containing JSON document files
        batch_size: Number of documents to process at once
        clear_existing: Whether to clear existing data before populating
    """
    # Default documents directory
    if documents_dir is None:
        base_dir = Path(__file__).parent.parent.parent
        documents_dir = (
            base_dir / "PrepareDocsForUpsert" / "OneToOneDocs" / "documents_to_upsert"
        )

    print("=" * 80)
    print("Neo4j Knowledge Graph Population")
    print("=" * 80)
    print()

    # Check if documents directory exists
    if not documents_dir.exists():
        logger.error(f"Documents directory not found: {documents_dir}")
        return

    # Initialize the knowledge graph
    print("Connecting to Neo4j...")
    kg = KnowledgeGraphDB()

    # Clear existing data if requested
    if clear_existing:
        print("\n⚠️  Clearing existing graph data...")
        kg.initialize_empty_graph()
        print("✓ Graph cleared and reinitialized")

    # Get initial statistics
    initial_stats = kg.get_graph_statistics()
    print("\nInitial graph state:")
    print(f"  Documents: {initial_stats['total_docs']}")
    print(f"  Projects: {initial_stats['total_projects']}")
    print(f"  Regions: {initial_stats['total_regions']}")
    print(f"  Communes: {initial_stats['total_communes']}")
    print(f"  Project Types: {initial_stats['total_project_types']}")
    print(f"  Typologies: {initial_stats['total_typologies']}")
    print(f"  Classes: {initial_stats['total_classes']}")

    # Load documents
    print(f"\nLoading documents from {documents_dir}...")
    documents = load_all_documents(documents_dir)
    print(f"Loaded {len(documents)} documents")

    # Analyze metadata
    unique_values = print_unique_metadata_values(documents)

    # Populate the knowledge graph
    print("\n" + "=" * 80)
    print("Populating Knowledge Graph")
    print("=" * 80)
    print(f"\nIngesting {len(documents)} documents in batches of {batch_size}...")

    try:
        kg.add_documents_batch(documents, batch_size=batch_size)
        print("✓ Documents successfully ingested")
    except Exception as e:
        logger.error(f"Error during ingestion: {e}")
        raise

    # Get final statistics
    final_stats = kg.get_graph_statistics()
    print("\n" + "=" * 80)
    print("Final Graph Statistics")
    print("=" * 80)
    print(
        f"  Documents: {final_stats['total_docs']} (+{final_stats['total_docs'] - initial_stats['total_docs']})"
    )
    print(
        f"  Projects: {final_stats['total_projects']} (+{final_stats['total_projects'] - initial_stats['total_projects']})"
    )
    print(
        f"  Regions: {final_stats['total_regions']} (+{final_stats['total_regions'] - initial_stats['total_regions']})"
    )
    print(
        f"  Communes: {final_stats['total_communes']} (+{final_stats['total_communes'] - initial_stats['total_communes']})"
    )
    print(
        f"  Project Types: {final_stats['total_project_types']} (+{final_stats['total_project_types'] - initial_stats['total_project_types']})"
    )
    print(
        f"  Typologies: {final_stats['total_typologies']} (+{final_stats['total_typologies'] - initial_stats['total_typologies']})"
    )
    print(
        f"  Classes: {final_stats['total_classes']} (+{final_stats['total_classes'] - initial_stats['total_classes']})"
    )

    # Test a sample query
    print("\n" + "=" * 80)
    print("Testing Sample Queries")
    print("=" * 80)

    test_queries = [
        "Impacto ambiental en la región",
        "Flora y fauna",
        "Medidas de mitigación",
    ]

    for query in test_queries:
        print(f"\nQuery: '{query}'")
        results = kg.hybrid_search(query, top_k=3, similarity_threshold=0.6)

        if results:
            for i, result in enumerate(results, 1):
                print(
                    f"  {i}. {result['filename'][:50]}... (score: {result['score']:.3f})"
                )
                print(f"     Project: {result['project']}")
                print(f"     Region: {result['region']}")
                print(f"     Commune: {result['commune']}")
                print(f"     Type: {result['project_type']}")
                print(f"     Typology: {result['typology']}")
                print(f"     Classes: {', '.join(result['classes'])}")
        else:
            print("  No results found")

    print("\n" + "=" * 80)
    print("✓ Knowledge graph population complete!")
    print(f"Total of {len(documents)} documents uploaded successfully.")
    print("✓ Ready for HybridCypherRetriever and GraphRAG queries")
    print("=" * 80)

    # Clean up
    kg.close()


def main() -> None:
    """Main entry point for the script."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Populate Neo4j knowledge graph with documents"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=50,
        help="Number of documents to process in each batch (default: 50)",
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear existing graph data before populating",
    )
    parser.add_argument(
        "--documents-dir",
        type=Path,
        help="Path to documents directory (default: PrepareDocsForUpsert/OneToOneDocs/documents_to_upsert)",
    )

    args = parser.parse_args()

    populate_knowledge_graph(
        documents_dir=args.documents_dir,
        batch_size=args.batch_size,
        clear_existing=args.clear,
    )


if __name__ == "__main__":
    main()
