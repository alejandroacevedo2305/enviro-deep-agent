"""GraphRAG tool for answering questions about the knowledge graph.

uv run tools/graph_rag.py
"""

# %%
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


from fastmcp import FastMCP

from Neo4j.retrievers.neo4j_graphrag import graph_rag_searcher

mcp = FastMCP("GraphRAGsearcher")


@mcp.tool
def get_graph_rag_answer(question: str) -> str:
    """Get the answer to a question using the GraphRAG searcher.

    Args:
        question: The question to ask the GraphRAG searcher.

    Returns:
        The answer from the GraphRAG searcher, including context if available.
    """
    result = graph_rag_searcher.search(
        question,
        retriever_config={"top_k": 20, "threshold": 0.6},
        return_context=True,
    )
    # Convert dict to JSON string to match return type annotation
    return json.dumps(result, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    """how to run the mcp server.

    uv run fastmcp run tools/graph_rag.py
    """

    # Q = "¿Cuál es el impacto ambiental del proyecto en la flora y fauna?"
    # output = get_graph_rag_answer(Q)
    # print("=" * 60 + "Question" + "=" * 60)
    # print(f"Question: {Q}")
    # print("=" * 60 + "Output" + "=" * 60)
    # print(output)
    mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")
