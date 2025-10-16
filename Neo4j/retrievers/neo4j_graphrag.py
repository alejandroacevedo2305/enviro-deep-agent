"""Neo4j GraphRAG compatible HybridCypherRetriever.

This module provides a retriever compatible with the neo4j-graphrag package
that performs hybrid search combining vector similarity with Cypher graph traversal.

poetry run python Neo4j/retrievers/neo4j_graphrag.py
"""

# %%
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

# Add parent directories to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from neo4j import Driver

# Load environment variables
load_dotenv(override=True)


class HybridCypherRetriever:
    """Hybrid Cypher Retriever compatible with neo4j-graphrag GraphRAG.

    This retriever combines vector similarity search with Cypher graph traversal
    to provide enriched context for RAG applications.
    """

    def __init__(
        self,
        driver: Driver,
        vector_index_name: str = "document_embeddings",
        fulltext_index_name: str = "document_content",
        embedder: OpenAIEmbeddings | None = None,
        retrieval_query: str | None = None,
        return_properties: list[str] | None = None,
    ):
        """Initialize the HybridCypherRetriever.

        Args:
            driver: Neo4j driver instance
            vector_index_name: Name of the vector index
            fulltext_index_name: Name of the full-text index
            embedder: Embeddings model (defaults to OpenAI)
            retrieval_query: Custom Cypher query for retrieval
            return_properties: List of properties to return from documents
        """
        self.driver = driver
        self.vector_index_name = vector_index_name
        self.fulltext_index_name = fulltext_index_name
        self.embedder = embedder or OpenAIEmbeddings(model="text-embedding-3-large")
        self.return_properties = return_properties or ["content", "filename"]

        # Default retrieval query that enriches context with graph traversal
        self.retrieval_query = (
            retrieval_query
            or """
        // Combine vector and full-text search
        CALL {
            // Vector similarity search
            CALL db.index.vector.queryNodes($vector_index_name, $top_k, $query_embedding)
            YIELD node as doc, score as vector_score
            RETURN doc, vector_score
            ORDER BY vector_score DESC
            LIMIT $top_k

            UNION

            // Full-text search
            CALL db.index.fulltext.queryNodes($fulltext_index_name, $query_text)
            YIELD node as doc, score as text_score
            RETURN doc, text_score / 10 as vector_score  // Normalize text score
            ORDER BY text_score DESC
            LIMIT $top_k
        }

        // Deduplicate and combine scores
        WITH doc, MAX(vector_score) as score
        WHERE score >= $threshold

        // Enrich with graph relationships
        OPTIONAL MATCH (doc)-[:HAS_CLASS]->(c:Class)
        OPTIONAL MATCH (doc)-[:IN_REGION]->(r:Region)
        OPTIONAL MATCH (doc)-[:IN_COMMUNE]->(cm:Commune)
        OPTIONAL MATCH (doc)-[:HAS_PROJECT_TYPE]->(pt:ProjectType)
        OPTIONAL MATCH (doc)-[:HAS_TIPOLOGIA]->(t:Typology)
        OPTIONAL MATCH (doc)-[:BELONGS_TO]->(p:Project)

        // Find related documents
        OPTIONAL MATCH (related:Document)-[:BELONGS_TO]->(p)
        WHERE related.id <> doc.id
        WITH doc, score, c, r, cm, pt, t, p,
             collect(DISTINCT related)[..3] as related_docs

        // Find similar documents by class
        OPTIONAL MATCH (similar:Document)-[:HAS_CLASS]->(c)
        WHERE similar.id <> doc.id AND c IS NOT NULL
        WITH doc, score, c, r, cm, pt, t, p, related_docs,
             collect(DISTINCT similar)[..3] as similar_docs

        RETURN doc, score,
               collect(DISTINCT c.name) as classes,
               r.name as region,
               cm.name as commune,
               pt.name as project_type,
               t.code as typology,
               p.name as project,
               [rd IN related_docs | rd.filename] as related_filenames,
               [sd IN similar_docs | sd.filename] as similar_filenames
        ORDER BY score DESC
        LIMIT $top_k
        """
        )

    def search(
        self,
        query_text: str,
        top_k: int = 5,
        filters: dict[str, Any] | None = None,
        **kwargs,
    ) -> list[dict[str, Any]]:
        """Search for documents using hybrid vector + full-text + graph approach.

        Args:
            query_text: Query text to search for
            top_k: Number of results to return
            filters: Additional filters (not used in this implementation)
            **kwargs: Additional parameters

        Returns:
            List of search results with enriched context
        """
        # Get threshold from kwargs or use default
        threshold = kwargs.get("threshold", 0.5)

        # Generate query embedding
        query_embedding = self.embedder.embed_query(query_text)

        # Execute the retrieval query
        with self.driver.session() as session:
            result = session.run(
                self.retrieval_query,
                {
                    "vector_index_name": self.vector_index_name,
                    "fulltext_index_name": self.fulltext_index_name,
                    "query_embedding": query_embedding,
                    "query_text": query_text,
                    "top_k": top_k,
                    "threshold": threshold,
                },
            )

            search_results = []
            for record in result:
                doc_node = record["doc"]

                # Build the content with enriched context
                content_parts = []

                # Add main document content
                if "content" in doc_node:
                    content_parts.append(doc_node["content"][:1000])

                # Add metadata as context
                metadata_context = []
                if record.get("project"):
                    metadata_context.append(f"Project: {record['project']}")
                if record.get("region"):
                    metadata_context.append(f"Region: {record['region']}")
                if record.get("commune"):
                    metadata_context.append(f"Commune: {record['commune']}")
                if record.get("project_type"):
                    metadata_context.append(f"Project Type: {record['project_type']}")
                if record.get("typology"):
                    metadata_context.append(f"Typology: {record['typology']}")
                if record.get("classes"):
                    metadata_context.append(f"Classes: {', '.join(record['classes'])}")

                if metadata_context:
                    content_parts.append("\nMetadata:\n" + "\n".join(metadata_context))

                # Add related documents context
                if record.get("related_filenames"):
                    content_parts.append(
                        f"\nRelated documents in same project: {', '.join(record['related_filenames'])}"
                    )
                if record.get("similar_filenames"):
                    content_parts.append(
                        f"\nSimilar documents (same class): {', '.join(record['similar_filenames'])}"
                    )

                search_results.append(
                    {
                        "content": "\n".join(content_parts),
                        "metadata": {
                            "doc_id": doc_node.get("id"),
                            "filename": doc_node.get("filename"),
                            "score": record.get("score", 0),
                            "project": record.get("project"),
                            "region": record.get("region"),
                            "commune": record.get("commune"),
                            "project_type": record.get("project_type"),
                            "typology": record.get("typology"),
                            "classes": record.get("classes", []),
                        },
                    }
                )

            return search_results


class GraphRAG:
    """GraphRAG pipeline for question answering using retriever and LLM."""

    def __init__(
        self,
        retriever: HybridCypherRetriever,
        llm: ChatOpenAI | None = None,
        prompt_template: str | None = None,
    ):
        """Initialize GraphRAG pipeline.

        Args:
            retriever: The retriever to use for context retrieval
            llm: Language model for generating answers
            prompt_template: Custom prompt template for the LLM
        """
        self.retriever = retriever
        self.llm = llm or ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )

        self.prompt_template = (
            prompt_template
            or """
You are a helpful assistant that answers questions based on the provided context.
Use the following context to answer the question. If you cannot answer the question
based on the context, say "I don't have enough information to answer this question."

Context:
{context}

Question: {question}

Answer: """
        )

    def search(
        self,
        query_text: str,
        retriever_config: dict[str, Any] | None = None,
        return_context: bool = False,
    ) -> dict[str, Any]:
        """Search for answer using retriever and LLM.

        Args:
            query_text: The question to answer
            retriever_config: Configuration for the retriever
            return_context: Whether to return the retrieved context

        Returns:
            Dictionary with answer and optionally context
        """
        # Get retriever configuration
        config = retriever_config or {}
        top_k = config.get("top_k", 5)
        threshold = config.get("threshold", 0.5)

        # Retrieve context
        search_results = self.retriever.search(
            query_text,
            top_k=top_k,
            threshold=threshold,
        )

        # Build context from search results
        context_parts = []
        for i, result in enumerate(search_results, 1):
            context_parts.append(f"Document {i}:\n{result['content']}\n")

        context = "\n".join(context_parts)

        # Generate answer using LLM
        prompt = self.prompt_template.format(
            context=context,
            question=query_text,
        )

        response = self.llm.invoke(prompt)

        result = {
            "answer": response.content,
            "query": query_text,
        }

        if return_context:
            result["context"] = search_results

        return result


from Neo4j.connection.conn import Neo4jConnection

# Initialize connection
conn = Neo4jConnection()
driver = conn.driver

# Initialize embedder
embedder = OpenAIEmbeddings(model="text-embedding-3-large")

# Initialize retriever
retriever = HybridCypherRetriever(
    driver=driver,
    vector_index_name="document_embeddings",
    fulltext_index_name="document_content",
    embedder=embedder,
)

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0,
)

# Custom RAG template
RAG_TEMPLATE = """
You are an expert environmental consultant analyzing environmental impact assessments.
Based on the provided context, answer the question accurately and comprehensively.
If the context doesn't contain enough information, clearly state what's missing.

Context from environmental documents:
{context}

Question: {question}

Provide a detailed answer based on the documents:
"""

# Initialize GraphRAG
graph_rag_searcher = GraphRAG(
    retriever=retriever,
    llm=llm,
    prompt_template=RAG_TEMPLATE,
)


if __name__ == "__main__":
    # Example queries
    queries = [
        "¿Cuál es el impacto ambiental del proyecto en la flora y fauna?",
    ]

    for query in queries:
        print(f"\n{'=' * 60}")
        print(f"Question: {query}")
        print("-" * 60)

        # Search with GraphRAG
        response = graph_rag_searcher.search(
            query_text=query,
            retriever_config={"top_k": 3, "threshold": 0.6},
            return_context=True,
        )

        print(f"Answer: {response['answer']}")

    # Clean up
    conn.close()
    print("\n✓ Example complete")
