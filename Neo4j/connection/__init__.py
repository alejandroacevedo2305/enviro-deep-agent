"""Neo4j connection module.

Simple and straightforward Neo4j connection management.
"""

# %%
from .conn import (
    Neo4jConnection,
    close_default_connection,
    get_connection,
)

__all__ = [
    "Neo4jConnection",
    "get_connection",
    "close_default_connection",
]
