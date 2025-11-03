"""cypher_runner.py
Utility helpers to execute ad-hoc Cypher queries against the Neo4j instance
configured through environment variables.

Usage example
-------------
>>> from cypher_runner import run_cypher
>>> run_cypher("MATCH (n) RETURN n LIMIT 5")

This module keeps a single Neo4j driver alive for the lifetime of the Python
process and shares it across calls.

uv run -m Neo4j.retrievers.cypher_runner
"""

# %%
from __future__ import annotations

import contextlib
import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv
from neo4j import Driver, GraphDatabase, Record
from neo4j.exceptions import ServiceUnavailable, SessionExpired

# --------------------------------------------------------------------------- #
# Driver initialisation (singleton)
# --------------------------------------------------------------------------- #

load_dotenv(override=True)

_NEO4J_URI: str = os.getenv("NEO4J_URI", "neo4j+s://neo4j-community.nviro.cl:7687")
_NEO4J_USER: str = os.getenv("NEO4J_USERNAME", "neo4j")
_NEO4J_PWD: str | None = os.getenv("NEO4J_PASSWORD")
_NEO4J_DATABASE: str = os.getenv("NEO4J_DATABASE", "neo4j")

if not _NEO4J_PWD:
    raise OSError("Missing Neo4j password. Set NEO4J_PASSWORD environment variable.")

_DRIVER: Driver = GraphDatabase.driver(
    _NEO4J_URI,
    auth=(_NEO4J_USER, _NEO4J_PWD),
    max_connection_lifetime=3600,
    max_connection_pool_size=50,
    connection_acquisition_timeout=60.0,
)
_DRIVER.verify_connectivity()

# --------------------------------------------------------------------------- #
# Public helper
# --------------------------------------------------------------------------- #


def run_cypher(
    query: str,
    parameters: dict[str, Any] | None = None,
    *,
    database: str | None = None,
    close_after: bool = False,
) -> list[dict[str, Any]]:
    """Run an arbitrary Cypher *read* query and return the results.

    Parameters
    ----------
    query:
        The Cypher query string to execute.
    parameters:
        Optional dictionary of parameters to pass to the query, following Neo4j
        best-practices for parameterised queries.
    database:
        Target database name. Defaults to the value from NEO4J_DATABASE
        environment variable or "neo4j".
    close_after:
        If *True*, the shared Neo4j driver will be closed immediately after the
        query finishes and results are collected. Set this to *False* (default)
        when you intend to run multiple queries in the same Python process.

    Returns:
    -------
    list[dict[str, Any]]
        List of result records as ordinary Python dictionaries, where keys are
        the column names specified in the Cypher `RETURN` clause.
    """
    if parameters is None:
        parameters = {}

    if database is None:
        database = _NEO4J_DATABASE

    global _DRIVER  # we may recreate it on failure

    try:
        with _DRIVER.session(database=database) as session:
            result = session.run(query, parameters)
            records: list[Record] = list(result)
    except (SessionExpired, ServiceUnavailable):
        # Attempt one automatic reconnection
        with contextlib.suppress(Exception):
            _DRIVER.close()

        _DRIVER = GraphDatabase.driver(
            _NEO4J_URI,
            auth=(_NEO4J_USER, _NEO4J_PWD),
            max_connection_lifetime=3600,
            max_connection_pool_size=50,
            connection_acquisition_timeout=60.0,
        )
        _DRIVER.verify_connectivity()

        with _DRIVER.session(database=database) as session:
            result = session.run(query, parameters)
            records = list(result)

    # Close the driver if requested *after* we have consumed all records.
    if close_after:
        close_driver()

    return [rec.data() for rec in records]


def close_driver() -> None:
    """Close the shared Neo4j driver (optional helper)."""
    _DRIVER.close()


if __name__ == "__main__":
    # --------------------------------------------------------------------------- #
    # Test basic connectivity and sample queries
    # --------------------------------------------------------------------------- #

    print(f"🔌 Connecting to Neo4j at {_NEO4J_URI}")
    print(f"📊 Database: {_NEO4J_DATABASE}\n")

    # Test 1: Basic connectivity
    print("📌 Test 1: Basic connectivity")
    print("Cypher: RETURN 1 AS test")
    rows = run_cypher("RETURN 1 AS test")
    print(f"→ Result: {rows}\n")

    # Test 2: Count all nodes
    print("📌 Test 2: Count all nodes")
    print("Cypher: MATCH (n) RETURN count(n) AS node_count")
    rows = run_cypher("MATCH (n) RETURN count(n) AS node_count")
    print(f"→ Result: {rows}\n")

    # Test 3: Get node labels
    print("📌 Test 3: Get node labels")
    print("Cypher: CALL db.labels() YIELD label RETURN label ORDER BY label")
    rows = run_cypher("CALL db.labels() YIELD label RETURN label ORDER BY label")
    print(f"→ Labels found: {[row['label'] for row in rows]}\n")

    # Test 4: Sample first 5 nodes
    print("📌 Test 4: Sample first 5 nodes")
    print("Cypher: MATCH (n) RETURN n LIMIT 5")
    rows = run_cypher("MATCH (n) RETURN n LIMIT 5")
    for idx, row in enumerate(rows, 1):
        print(f"  Node {idx}: {row}\n")

    # Optional: Load and run queries from YAML if file exists
    yaml_path = Path(__file__).with_name("sample_queries.yaml")
    if yaml_path.exists():
        print("📌 Running queries from sample_queries.yaml\n")
        sample_queries = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        for item in sample_queries:
            title = item["pregunta"]
            cypher = item["cypher_query"]
            print(f"📌 {title}")
            print(f"Cypher: {cypher.strip()}")
            rows = run_cypher(cypher)
            print("→ Results:")
            for row in rows:
                print(f"  {row}")
            print()

    # Close driver at the very end
    print("🔒 Closing Neo4j driver connection")
    close_driver()
