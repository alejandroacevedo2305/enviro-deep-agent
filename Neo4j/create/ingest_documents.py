"""Simple script to ingest documents into the Neo4j knowledge graph.

This script loads documents from the documents_to_upsert directory
and populates the Neo4j knowledge graph for hybrid search.

uv run python Neo4j/create/ingest_documents.py
"""

# %%
from __future__ import annotations

import sys
from pathlib import Path

# Add parent directories to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from KnowledgeGraphDB import KnowledgeGraphDB

from PrepareDocsForUpsert.OneToOneDocs.load_documents import (
    load_all_documents,
    load_document_from_json,
)


def ingest_sample_documents(num_documents: int = 10) -> None:
    """Ingest a sample of documents into the knowledge graph.

    Args:
        num_documents: Number of documents to ingest (for testing)
    """
    # Define paths
    base_dir = Path(__file__).parent.parent.parent
    documents_dir = (
        base_dir / "PrepareDocsForUpsert" / "OneToOneDocs" / "documents_to_upsert"
    )

    print("=" * 80)
    print("Document Ingestion to Neo4j Knowledge Graph")
    print("=" * 80)
    print()

    # Initialize the knowledge graph
    print("Connecting to Neo4j...")
    kg = KnowledgeGraphDB()

    # Get initial statistics
    initial_stats = kg.get_graph_statistics()
    print("Initial graph state:")
    print(f"  Documents: {initial_stats['total_docs']}")
    print(f"  Projects: {initial_stats['total_projects']}")
    print(f"  Regions: {initial_stats['total_regions']}")
    print(f"  Classes: {initial_stats['total_classes']}")
    print()

    # Load sample documents
    print(f"Loading {num_documents} sample documents...")
    json_files = sorted(documents_dir.glob("*.json"))[:num_documents]

    if not json_files:
        print("ERROR: No documents found!")
        return

    documents = []
    for json_file in json_files:
        doc = load_document_from_json(json_file)
        documents.append(doc)
        print(f"  Loaded: {json_file.name}")

    print()

    # Ingest documents into the knowledge graph
    print("Ingesting documents into knowledge graph...")
    kg.add_documents_batch(documents, batch_size=5)

    # Get final statistics
    final_stats = kg.get_graph_statistics()
    print()
    print("Final graph state:")
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
        f"  Classes: {final_stats['total_classes']} (+{final_stats['total_classes'] - initial_stats['total_classes']})"
    )
    print()

    # Test hybrid search
    print("=" * 80)
    print("Testing Hybrid Search")
    print("=" * 80)

    test_queries = [
        "Flora y vegetación",
        "Fauna en la región",
        "Línea base ambiental",
    ]

    for query in test_queries:
        print(f"\nSearching for: '{query}'")
        results = kg.hybrid_search(query, top_k=3)

        if results:
            for i, result in enumerate(results, 1):
                print(f"  {i}. {result['filename']} (score: {result['score']:.3f})")
                print(f"     Project: {result['project']}")
                print(f"     Region: {result['region']}")
                print(f"     Classes: {', '.join(result['classes'])}")
        else:
            print("  No results found")

    print()
    print("✓ Document ingestion complete!")

    # Clean up
    kg.close()


def ingest_all_documents() -> None:
    """Ingest ALL documents into the knowledge graph."""
    # Define paths
    base_dir = Path(__file__).parent.parent.parent
    documents_dir = (
        base_dir / "PrepareDocsForUpsert" / "OneToOneDocs" / "documents_to_upsert"
    )

    print("=" * 80)
    print("Full Document Ingestion to Neo4j Knowledge Graph")
    print("=" * 80)
    print()

    # Initialize the knowledge graph
    print("Connecting to Neo4j...")
    kg = KnowledgeGraphDB()

    # Clear and reinitialize for full ingestion
    print("Initializing empty graph for full ingestion...")
    kg.initialize_empty_graph()

    # Load all documents
    print("Loading all documents...")
    documents = load_all_documents(documents_dir)

    # Ingest all documents
    print(f"Ingesting {len(documents)} documents into knowledge graph...")
    kg.add_documents_batch(documents, batch_size=100)

    # Get final statistics
    final_stats = kg.get_graph_statistics()
    print()
    print("Final graph statistics:")
    print(f"  Total Documents: {final_stats['total_docs']}")
    print(f"  Total Projects: {final_stats['total_projects']}")
    print(f"  Total Regions: {final_stats['total_regions']}")
    print(f"  Total Classes: {final_stats['total_classes']}")

    print()
    print("✓ Full document ingestion complete!")
    print("✓ Knowledge graph ready for hybrid search!")

    # Clean up
    kg.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Ingest documents into Neo4j knowledge graph"
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=10,
        help="Number of sample documents to ingest (default: 10)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Ingest all documents (overrides --sample)",
    )

    args = parser.parse_args()

    if args.all:
        ingest_all_documents()
    else:
        ingest_sample_documents(args.sample)
