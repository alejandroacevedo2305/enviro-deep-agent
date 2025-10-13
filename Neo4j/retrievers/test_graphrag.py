"""Test script for Neo4j GraphRAG with HybridCypherRetriever.

This script demonstrates the usage pattern:
    retriever = HybridCypherRetriever(...)
    graph_rag = GraphRAG(retriever=retriever, llm=llm, prompt_template=rag_template)
    response = graph_rag.search(...)


uv run python Neo4j/retrievers/test_graphrag.py
"""

# %%
from __future__ import annotations

import os
import sys
from pathlib import Path

# Add parent directories to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from Neo4j.connection.conn import Neo4jConnection
from Neo4j.retrievers.neo4j_graphrag_retriever import GraphRAG, HybridCypherRetriever

# Load environment variables
load_dotenv(override=True)


def main():
    """Main function demonstrating GraphRAG usage."""
    print("=" * 80)
    print("Neo4j GraphRAG Demo - Environmental Impact Assessment Analysis")
    print("=" * 80)
    print()

    # Step 1: Initialize Neo4j connection
    print("Step 1: Initializing Neo4j connection...")
    conn = Neo4jConnection()
    driver = conn.driver
    print("✓ Connected to Neo4j")
    print()

    # Step 2: Initialize embedder
    print("Step 2: Setting up embeddings model...")
    embedder = OpenAIEmbeddings(
        model="text-embedding-3-large",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )
    print("✓ Embeddings model ready")
    print()

    # Step 3: Initialize retriever
    print("Step 3: Configuring HybridCypherRetriever...")
    retriever = HybridCypherRetriever(
        driver=driver,
        vector_index_name="document_embeddings",
        fulltext_index_name="document_content",
        embedder=embedder,
    )
    print("✓ Retriever configured")
    print()

    # Step 4: Initialize LLM
    print("Step 4: Setting up language model...")
    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )
    print("✓ Language model ready")
    print()

    # Step 5: Define custom RAG template
    print("Step 5: Configuring RAG template...")
    rag_template = """
You are an expert environmental consultant specializing in Environmental Impact Assessments (EIA)
for development projects in Chile. You have deep knowledge of Chilean environmental regulations,
SEIA (Sistema de Evaluación de Impacto Ambiental) requirements, and best practices for environmental
protection and mitigation measures.

Based on the provided context from environmental documents, answer the question with:
1. Specific details from the documents
2. Relevant regulatory context when applicable
3. Clear identification of any gaps in the available information

Context from environmental assessment documents:
{context}

Question: {question}

Provide a comprehensive answer in Spanish, as these are Chilean projects:
"""
    print("✓ RAG template configured")
    print()

    # Step 6: Initialize GraphRAG
    print("Step 6: Initializing GraphRAG pipeline...")
    graph_rag = GraphRAG(
        retriever=retriever,
        llm=llm,
        prompt_template=rag_template,
    )
    print("✓ GraphRAG pipeline ready")
    print()

    # Step 7: Test queries
    print("=" * 80)
    print("Testing GraphRAG with Environmental Queries")
    print("=" * 80)

    queries = [
        "¿Cuáles son los principales impactos ambientales identificados en los proyectos?",
        "¿Qué especies de flora y fauna se encuentran en el área de influencia?",
        "¿Cuáles son las medidas de mitigación propuestas para proteger el medio ambiente?",
        "¿En qué comunas y regiones se desarrollan los proyectos?",
        "¿Qué tipo de proyectos están siendo evaluados?",
    ]

    for i, query in enumerate(queries, 1):
        print(f"\n{'=' * 70}")
        print(f"Query {i}: {query}")
        print("-" * 70)

        # Perform search with GraphRAG
        response = graph_rag.search(
            query_text=query,
            retriever_config={
                "top_k": 5,  # Retrieve top 5 documents
                "threshold": 0.6,  # Minimum similarity threshold
            },
            return_context=True,  # Return the retrieved context
        )

        # Display answer
        print("\n📝 Answer:")
        print(response["answer"])

        # Display retrieved documents
        if "context" in response and response["context"]:
            print("\n📚 Retrieved Documents:")
            for j, ctx in enumerate(response["context"], 1):
                metadata = ctx["metadata"]
                print(f"\n  {j}. Document: {metadata.get('filename', 'Unknown')}")
                print(f"     Score: {metadata.get('score', 0):.3f}")
                print(f"     Project: {metadata.get('project', 'N/A')}")
                print(f"     Region: {metadata.get('region', 'N/A')}")
                print(f"     Commune: {metadata.get('commune', 'N/A')}")
                print(f"     Type: {metadata.get('project_type', 'N/A')}")
                print(f"     Classes: {', '.join(metadata.get('classes', []))}")

    # Step 8: Demonstrate retriever configuration options
    print("\n" + "=" * 80)
    print("Advanced Configuration Example")
    print("=" * 80)

    # Custom retrieval query focusing on specific relationships
    custom_retrieval_query = """
    // Focus on documents with Flora and Fauna classes
    MATCH (doc:Document)-[:HAS_CLASS]->(c:Class)
    WHERE c.name IN ['Flora', 'Fauna', 'Flora y Vegetación', 'Línea Base']

    // Get vector similarity
    CALL db.index.vector.queryNodes($vector_index_name, $top_k, $query_embedding)
    YIELD node as similar_doc, score
    WHERE similar_doc.id = doc.id AND score >= $threshold

    // Enrich with relationships
    OPTIONAL MATCH (doc)-[:IN_REGION]->(r:Region)
    OPTIONAL MATCH (doc)-[:BELONGS_TO]->(p:Project)

    RETURN doc, score,
           collect(DISTINCT c.name) as classes,
           r.name as region,
           p.name as project,
           [] as related_filenames,
           [] as similar_filenames
    ORDER BY score DESC
    LIMIT $top_k
    """

    # Create specialized retriever for flora/fauna queries
    specialized_retriever = HybridCypherRetriever(
        driver=driver,
        vector_index_name="document_embeddings",
        fulltext_index_name="document_content",
        embedder=embedder,
        retrieval_query=custom_retrieval_query,
    )

    # Create specialized GraphRAG
    specialized_rag = GraphRAG(
        retriever=specialized_retriever,
        llm=llm,
        prompt_template=rag_template,
    )

    print("\nTesting specialized retriever for flora/fauna queries:")
    specialized_query = "¿Qué información hay sobre la biodiversidad en los proyectos?"

    print(f"\nQuery: {specialized_query}")
    print("-" * 70)

    response = specialized_rag.search(
        query_text=specialized_query,
        retriever_config={"top_k": 3, "threshold": 0.5},
        return_context=True,
    )

    print("\n📝 Answer:")
    print(
        response["answer"][:500] + "..."
        if len(response["answer"]) > 500
        else response["answer"]
    )

    # Clean up
    conn.close()
    print("\n" + "=" * 80)
    print("✓ GraphRAG demonstration complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
