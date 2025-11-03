"""LangChain tool for hybrid vector + graph search in Neo4j.

This module provides a LangChain-compatible tool that performs semantic search
combined with graph traversal for rich contextual retrieval.

uv run -m tools.hybrid_cypher_retriever
"""

# %%
from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_core.tools import StructuredTool
from neo4j import GraphDatabase

from Neo4j.retrievers.HybridCypher import CustomHybridCypherRetriever

# Load environment variables
load_dotenv(override=True)

# Initialize Neo4j driver (singleton pattern)
_NEO4J_URI: str = os.getenv("NEO4J_URI", "neo4j+s://neo4j-community.nviro.cl:7687")
_NEO4J_USER: str = os.getenv("NEO4J_USERNAME", "neo4j")
_NEO4J_PWD: str | None = os.getenv("NEO4J_PASSWORD")

if not _NEO4J_PWD:
    raise OSError("Missing Neo4j password. Set NEO4J_PASSWORD environment variable.")

_DRIVER = GraphDatabase.driver(
    _NEO4J_URI,
    auth=(_NEO4J_USER, _NEO4J_PWD),
    max_connection_lifetime=3600,
    max_connection_pool_size=50,
    connection_acquisition_timeout=60.0,
)


def hybrid_search_documents(natural_language_query: str) -> str:
    """Perform hybrid semantic vector search with graph traversal in Neo4j.

    This tool performs semantic similarity search using vector embeddings combined
    with knowledge graph traversal to retrieve highly relevant environmental impact
    assessment documents with enriched contextual information.

    Query Guidelines
    ----------------
    The query should be a **long, semantically enriched natural language question**
    that is augmented with synonyms and semantically related meanings to improve
    RAG (Retrieval Augmented Generation) performance.

    **IMPORTANT**: This query is used for semantic similarity search in the
    vectorstore. The more descriptive and detailed your query, the better the
    retrieval results will be.

    Good query examples:
    - "¿Cuáles son los impactos ambientales sobre la flora y vegetación nativa,
      incluyendo bosques autóctonos, especies endémicas, y formaciones xerofíticas
      en proyectos mineros de la región de Antofagasta?"

    - "Describe las medidas de mitigación, compensación y restauración ecológica
      implementadas para proteger la fauna vertebrada, avifauna, mamíferos y
      especies en peligro de extinción en proyectos de energía renovable"

    - "¿Qué documentos de línea base ambiental discuten la calidad del agua,
      recursos hídricos, hidrología superficial y subterránea, limnología y
      ecosistemas acuáticos en proyectos de la región metropolitana?"

    Poor query examples (too short/generic):
    - "flora"
    - "impacto ambiental"
    - "documentos"

    How It Works
    ------------
    1. Converts your natural language query into a vector embedding
    2. Performs similarity search against document embeddings in Neo4j vectorstore
    3. Traverses the knowledge graph to enrich results with:
       - Project information
       - Regional and communal context
       - Document classifications and typologies
       - Related documents from the same project
       - Similar documents with shared classifications
    4. Returns top 20 most relevant documents with full content and metadata

    Parameters
    ----------
    natural_language_query:
        A detailed, semantically rich natural language query describing what you
        want to find. Should include synonyms, related concepts, and specific
        details about the topic (e.g., flora types, fauna species, project types,
        regions, environmental impacts, etc.).

    Returns
    -------
    str
        Formatted string containing the top 20 search results. Each result includes:
        - Similarity score (0.0 to 1.0)
        - Document filename
        - Full metadata (project, region, commune, classifications, related docs)
        - Complete document content with enriched contextual information

    Examples
    --------
    Search for flora and fauna baseline studies:
    >>> hybrid_search_documents(
    ...     "estudios de línea base de flora y vegetación nativa, bosques, "
    ...     "especies endémicas, así como fauna vertebrada, avifauna, mamíferos "
    ...     "terrestres y especies en conservación en proyectos ambientales"
    ... )

    Search for mining project environmental impacts:
    >>> hybrid_search_documents(
    ...     "impactos ambientales de proyectos mineros, extracción de minerales, "
    ...     "faenas mineras, relaves, emisiones, calidad del aire, recursos hídricos "
    ...     "y medidas de mitigación en la región de Antofagasta y Atacama"
    ... )
    """
    # Initialize retriever with the global driver
    retriever = CustomHybridCypherRetriever(driver=_DRIVER)

    # Perform hybrid search with top_k=20
    results = retriever.search(query_text=natural_language_query, top_k=20)

    # Format output similar to lines 250-254 in HybridCypher.py
    output_parts = []
    output_parts.append(f"Found {len(results)} relevant documents:\n")
    output_parts.append("=" * 80)

    for i, result in enumerate(results, 1):
        output_parts.append(f"\nResult {i} (Score: {result['score']:.3f}):")
        output_parts.append(f"File: {result['filename']}")
        output_parts.append(f"Metadata: {result['metadata']}")
        output_parts.append("Content:")
        output_parts.append(result["content"])
        output_parts.append("-" * 80)

    return "\n".join(output_parts)


# Create the LangChain tool
hybrid_search_tool = StructuredTool.from_function(
    func=hybrid_search_documents,
    name="hybrid_search_documents",
    description=(
        "Perform semantic similarity search in Neo4j vectorstore combined with "
        "knowledge graph traversal. Use this tool to find relevant environmental "
        "documents by providing a long, detailed natural language query enriched "
        "with synonyms and related concepts. Returns top 20 documents with full "
        "content and enriched metadata including project info, regions, classes, "
        "and related documents."
    ),
)


if __name__ == "__main__":
    # Demonstration of the tool
    print("🔍 Testing Hybrid Search Tool\n")
    print("=" * 80)

    # Test query 1: Flora and fauna
    print("\n📌 Test 1: Flora and fauna baseline studies")
    print("-" * 80)
    query1 = (
        "estudios de línea base de flora y vegetación nativa, bosques autóctonos, "
        "especies endémicas, formaciones xerofíticas, así como fauna vertebrada, "
        "avifauna, mamíferos terrestres y especies en conservación"
    )
    print(f"Query: {query1}\n")

    result1 = hybrid_search_tool.invoke({"natural_language_query": query1})
    # Print only first 2000 characters to avoid overwhelming output
    print(result1[:2000])
    print("\n[... truncated for brevity ...]\n")

    # Test query 2: Mining projects
    print("\n📌 Test 2: Mining project environmental impacts")
    print("-" * 80)
    query2 = (
        "impactos ambientales de proyectos mineros, extracción de minerales, "
        "faenas mineras, relaves, emisiones atmosféricas, calidad del aire, "
        "recursos hídricos superficiales y subterráneos, medidas de mitigación "
        "y compensación en regiones del norte de Chile"
    )
    print(f"Query: {query2}\n")

    result2 = hybrid_search_tool.invoke({"natural_language_query": query2})
    # Print only first 2000 characters
    print(result2[:2000])
    print("\n[... truncated for brevity ...]\n")

    # Test query 3: Energy projects
    print("\n📌 Test 3: Renewable energy projects")
    print("-" * 80)
    query3 = (
        "proyectos de energía renovable, centrales generadoras, parques eólicos, "
        "plantas fotovoltaicas, energía solar, impacto ambiental, líneas de "
        "transmisión eléctrica, evaluación ambiental"
    )
    print(f"Query: {query3}\n")

    result3 = hybrid_search_tool.invoke({"natural_language_query": query3})
    # Print only first 2000 characters
    print(result3[:2000])
    print("\n[... truncated for brevity ...]\n")

    print("=" * 80)
    print("✅ All tests completed successfully!")
    print("\n💡 Note: Results are truncated for display purposes.")
    print("   The actual tool returns full content for all 20 documents.")
