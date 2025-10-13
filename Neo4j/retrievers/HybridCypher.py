"""HybridCypher Retriever for Neo4j GraphRAG.

This module provides a retriever that can be used with neo4j-graphrag
for hybrid search combining vector similarity and Cypher graph traversal.
"""

# %%
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Add parent directories to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from neo4j import Driver


class CustomHybridCypherRetriever:
    """Custom retriever for hybrid search with Neo4j using Cypher queries.

    This retriever combines vector similarity search with graph traversal
    to provide rich context for RAG applications.
    """

    def __init__(
        self,
        driver: Driver,
        index_name: str = "document_embeddings",
        embedder: OpenAIEmbeddings | None = None,
        retrieval_query: str | None = None,
    ):
        """Initialize the hybrid Cypher retriever.

        Args:
            driver: Neo4j driver instance
            index_name: Name of the vector index
            embedder: Embeddings model (defaults to OpenAI)
            retrieval_query: Custom Cypher query for retrieval
        """
        self.driver = driver
        self.index_name = index_name
        self.embedder = embedder or OpenAIEmbeddings(model="text-embedding-3-large")

        # Default retrieval query that traverses the graph
        self.retrieval_query = (
            retrieval_query
            or """
        // Start with vector similarity search
        CALL db.index.vector.queryNodes($index_name, $top_k, $query_embedding)
        YIELD node as doc, score
        WHERE score >= $threshold

        // Traverse graph to get related context
        OPTIONAL MATCH (doc)-[:HAS_CLASS]->(c:Class)
        OPTIONAL MATCH (doc)-[:IN_REGION]->(r:Region)
        OPTIONAL MATCH (doc)-[:IN_COMMUNE]->(cm:Commune)
        OPTIONAL MATCH (doc)-[:HAS_PROJECT_TYPE]->(pt:ProjectType)
        OPTIONAL MATCH (doc)-[:HAS_TIPOLOGIA]->(t:Typology)
        OPTIONAL MATCH (doc)-[:BELONGS_TO]->(p:Project)

        // Find related documents from same project or region
        OPTIONAL MATCH (related:Document)-[:BELONGS_TO]->(p)
        WHERE related.id <> doc.id
        WITH doc, score, c, r, cm, pt, t, p,
             collect(DISTINCT related.filename)[..3] as related_docs

        // Find documents with same classes
        OPTIONAL MATCH (similar:Document)-[:HAS_CLASS]->(c)
        WHERE similar.id <> doc.id
        WITH doc, score, c, r, cm, pt, t, p, related_docs,
             collect(DISTINCT similar.filename)[..3] as similar_docs

        RETURN doc.id as doc_id,
               doc.filename as filename,
               doc.content as content,
               doc.projectName as project_name,
               score,
               collect(DISTINCT c.name) as classes,
               r.name as region,
               cm.name as commune,
               pt.name as project_type,
               t.code as typology,
               p.name as project,
               related_docs,
               similar_docs
        ORDER BY score DESC
        LIMIT $top_k
        """
        )

    def search(
        self,
        query_text: str,
        top_k: int = 5,
        threshold: float = 0.6,
        **kwargs,
    ) -> list[dict[str, Any]]:
        """Search for documents using hybrid vector + graph approach.

        Args:
            query_text: Query text to search for
            top_k: Number of results to return
            threshold: Similarity threshold
            **kwargs: Additional parameters

        Returns:
            List of search results with enriched context
        """
        # Generate query embedding
        query_embedding = self.embedder.embed_query(query_text)

        # Execute the retrieval query
        with self.driver.session() as session:
            result = session.run(
                self.retrieval_query,
                {
                    "index_name": self.index_name,
                    "query_embedding": query_embedding,
                    "top_k": top_k,
                    "threshold": threshold,
                },
            )

            documents = []
            for record in result:
                # Build enriched context
                context_parts = []

                # Add main content
                context_parts.append(f"Document: {record['filename']}")
                context_parts.append(f"Project: {record['project_name']}")
                context_parts.append(f"Content: {record['content'][:500]}...")

                # Add metadata context
                if record["classes"]:
                    context_parts.append(f"Classes: {', '.join(record['classes'])}")
                if record["region"]:
                    context_parts.append(f"Region: {record['region']}")
                if record["commune"]:
                    context_parts.append(f"Commune: {record['commune']}")
                if record["project_type"]:
                    context_parts.append(f"Project Type: {record['project_type']}")
                if record["typology"]:
                    context_parts.append(f"Typology: {record['typology']}")

                # Add related documents context
                if record["related_docs"]:
                    context_parts.append(
                        f"Related documents in same project: {', '.join(record['related_docs'])}"
                    )
                if record["similar_docs"]:
                    context_parts.append(
                        f"Similar documents (same class): {', '.join(record['similar_docs'])}"
                    )

                documents.append(
                    {
                        "doc_id": record["doc_id"],
                        "filename": record["filename"],
                        "content": "\n".join(context_parts),
                        "score": record["score"],
                        "metadata": {
                            "project": record["project"],
                            "region": record["region"],
                            "commune": record["commune"],
                            "project_type": record["project_type"],
                            "typology": record["typology"],
                            "classes": record["classes"],
                            "related_docs": record["related_docs"],
                            "similar_docs": record["similar_docs"],
                        },
                    }
                )

            return documents

    def get_search_results(
        self,
        query_text: str,
        top_k: int = 5,
        **kwargs,
    ) -> list[Document]:
        """Get search results as LangChain Documents.

        Args:
            query_text: Query text to search for
            top_k: Number of results to return
            **kwargs: Additional parameters

        Returns:
            List of LangChain Document objects
        """
        results = self.search(query_text, top_k=top_k, **kwargs)

        documents = []
        for result in results:
            doc = Document(
                page_content=result["content"],
                metadata={
                    "doc_id": result["doc_id"],
                    "filename": result["filename"],
                    "score": result["score"],
                    **result["metadata"],
                },
            )
            documents.append(doc)

        return documents


def example_usage():
    """Example of using the HybridCypher retriever."""

    from Neo4j.connection.conn import Neo4jConnection

    print("=" * 80)
    print("HybridCypher Retriever Example")
    print("=" * 80)
    print()

    # Initialize connection
    conn = Neo4jConnection()
    driver = conn.driver

    # Initialize retriever
    retriever = CustomHybridCypherRetriever(driver)

    # Example queries
    queries = [
        "Impacto ambiental del proyecto",
        "Flora y fauna en la región",
        "Medidas de mitigación",
    ]

    for query in queries:
        print(f"\nSearching for: '{query}'")
        print("-" * 40)

        results = retriever.search(query, top_k=2)

        for i, result in enumerate(results, 1):
            print(f"\nResult {i} (Score: {result['score']:.3f}):")
            print(f"File: {result['filename']}")
            print(f"Metadata: {result['metadata']}")
            print("Context preview:")
            print(result["content"][:300] + "...")

    # Clean up
    conn.close()
    print("\n✓ Example complete")


if __name__ == "__main__":
    example_usage()
