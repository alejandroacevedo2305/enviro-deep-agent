"""ReAct agent for environmental document retrieval and analysis.

This agent uses LangChain's create_agent with ReAct pattern to interact with
Neo4j knowledge graph and vector store. The agent can perform semantic searches
and execute Cypher queries to answer questions about Chilean environmental
impact assessment documents.

The agent responds in Spanish and iteratively uses available tools until
completing user requests or determining no further progress can be made.

uv run -m agents.deep_agent
"""

# %%
from __future__ import annotations

from deepagents import create_deep_agent
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from tools.cypher_query_runner import cypher_query_tool
from tools.hybrid_cypher_retriever import hybrid_search_tool

# Load environment variables
load_dotenv(override=True)


SYSTEM_PROMPT = """\
You are an expert researcher. Your job is to conduct \
thorough research, and then write a polished report. \
"""

model = init_chat_model(model="gpt-4.1")
tools = [cypher_query_tool, hybrid_search_tool]
agent = create_deep_agent(
    model=model,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
)

if __name__ == "__main__":
    print(
        agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "¿Cuál es el impacto ambiental del proyecto en la flora y fauna?",
                    }
                ]
            }
        )
    )
