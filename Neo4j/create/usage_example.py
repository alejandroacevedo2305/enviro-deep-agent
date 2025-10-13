"""Simple usage example for the Neo4j Knowledge Graph.

This script demonstrates how to use the knowledge graph for hybrid search.
"""

# %%
from __future__ import annotations

import sys
from pathlib import Path

# Add parent directories to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from KnowledgeGraphDB import KnowledgeGraphDB

from PrepareDocsForUpsert.OneToOneDocs.load_documents import load_document_from_json


def main() -> None:
    """Demonstrate knowledge graph usage."""
    print("=" * 80)
    print("Neo4j Knowledge Graph - Usage Example")
    print("=" * 80)
    print()

    # Initialize the knowledge graph
    print("Connecting to Neo4j...")
    kg = KnowledgeGraphDB(
        embedding_model="text-embedding-3-large",
        llm_model="gpt-4o-mini",
    )

    # Check current state
    stats = kg.get_graph_statistics()
    print("Current graph state:")
    print(f"  Documents: {stats['total_docs']}")
    print(f"  Projects: {stats['total_projects']}")
    print(f"  Regions: {stats['total_regions']}")
    print(f"  Classes: {stats['total_classes']}")
    print()

    # Example 1: Hybrid Search
    print("=" * 80)
    print("Example 1: Hybrid Search")
    print("=" * 80)

    queries = [
        "Flora y fauna en el área del proyecto",
        "Impacto ambiental del proyecto",
        "Medidas de mitigación",
        "Línea base ambiental",
        "Especies en categoría de conservación",
    ]

    for query in queries:
        print(f"\nSearching for: '{query}'")
        results = kg.hybrid_search(query, top_k=3, similarity_threshold=0.6)

        if results:
            for i, result in enumerate(results, 1):
                print(
                    f"  {i}. {result['filename'][:50]}... (score: {result['score']:.3f})"
                )
                print(f"     Project: {result['project']}")
                print(f"     Classes: {', '.join(result['classes'])}")
                # Show snippet of content
                content_snippet = result["content"][:200].replace("\n", " ")
                print(f"     Content: {content_snippet}...")
        else:
            print("  No results found above threshold")

    # Example 2: Add a new document
    print()
    print("=" * 80)
    print("Example 2: Adding a New Document")
    print("=" * 80)

    # Load a sample document
    base_dir = Path(__file__).parent.parent.parent
    documents_dir = (
        base_dir / "PrepareDocsForUpsert" / "OneToOneDocs" / "documents_to_upsert"
    )

    json_files = list(documents_dir.glob("*.json"))
    if json_files:
        # Find a document not yet in the graph
        new_doc_file = None
        for json_file in json_files[10:20]:  # Check files 10-20
            doc_id = json_file.stem
            # Check if document exists
            check_query = """
            MATCH (d:Document {id: $doc_id})
            RETURN count(d) as exists
            """
            records, _, _ = kg.connection.execute_query(check_query, {"doc_id": doc_id})
            if records[0]["exists"] == 0:
                new_doc_file = json_file
                break

        if new_doc_file:
            print(f"Adding new document: {new_doc_file.name}")
            new_doc = load_document_from_json(new_doc_file)
            doc_id = kg.add_document(new_doc)
            print(f"✓ Added document with ID: {doc_id}")

            # Verify it was added
            stats_after = kg.get_graph_statistics()
            print(f"Documents after addition: {stats_after['total_docs']}")

    # Example 3: Graph Traversal Query
    print()
    print("=" * 80)
    print("Example 3: Graph Traversal - Find Related Documents")
    print("=" * 80)

    # Find documents from the same project
    project_query = """
    MATCH (p:Project)
    WITH p LIMIT 1
    MATCH (d:Document)-[:BELONGS_TO]->(p)
    MATCH (d)-[:HAS_CLASS]->(c:Class)
    RETURN p.name as project,
           count(DISTINCT d) as doc_count,
           collect(DISTINCT c.name) as classes
    """

    records, _, _ = kg.connection.execute_query(project_query)
    if records:
        for record in records:
            print(f"Project: {record['project']}")
            print(f"  Documents: {record['doc_count']}")
            print(f"  Classes: {', '.join(record['classes'])}")

    # Example 4: Find documents by class
    print()
    print("=" * 80)
    print("Example 4: Find Documents by Class")
    print("=" * 80)

    class_query = """
    MATCH (c:Class)
    WITH c
    MATCH (d:Document)-[:HAS_CLASS]->(c)
    RETURN c.name as class_name,
           count(d) as doc_count,
           collect(DISTINCT d.filename)[..3] as sample_files
    ORDER BY doc_count DESC
    """

    records, _, _ = kg.connection.execute_query(class_query)
    if records:
        for record in records:
            print(f"Class: {record['class_name']}")
            print(f"  Document count: {record['doc_count']}")
            if record["sample_files"]:
                print("  Sample files:")
                for filename in record["sample_files"]:
                    print(f"    - {filename}")

    print()
    print("=" * 80)
    print("✓ Knowledge Graph is ready for hybrid search!")
    print("=" * 80)

    # Clean up
    kg.close()


if __name__ == "__main__":
    main()
