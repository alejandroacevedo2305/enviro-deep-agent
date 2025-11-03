"""Simple tests for `run_cypher` from `Neo4j.retrievers.cypher_runner`.

These tests run a few basic queries against the configured Neo4j instance.
Ensure environment variables `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`,
and `NEO4J_DATABASE` are set (a .env file is also supported).

uv run Neo4j/retrievers/cypher_runner_tests.py
"""

# %%
from __future__ import annotations

from pathlib import Path

import yaml

from Neo4j.retrievers.cypher_runner import run_cypher


def run_yaml_examples() -> None:
    """Load and run sample queries from the YAML file next to this module."""
    yaml_path = Path(__file__).with_name("sample_queries.yaml")
    if not yaml_path.exists():
        print("No sample_queries.yaml found; skipping YAML-driven examples.")
        return

    items = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    for item in items:
        title = item.get("pregunta", "Untitled")
        cypher = item.get("cypher_query", "")
        print(f"\n📌 {title}")
        print("Cypher:")
        print(cypher.strip())
        rows = run_cypher(cypher)
        print("→ Results:")
        for row in rows:
            print(f"  {row}")


if __name__ == "__main__":
    print("🔎 Running queries from sample_queries.yaml")
    run_yaml_examples()
