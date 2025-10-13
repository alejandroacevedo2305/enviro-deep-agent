"""Test suite for Neo4j connection module.

Run with:
    uv run -m Neo4j.connection.test_conn
"""

# %%
import logging

import pytest
from dotenv import load_dotenv
from neo4j.exceptions import ClientError

from .conn import Neo4jConnection, close_default_connection, get_connection

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv(override=True)


class TestNeo4jConnection:
    """Test suite for Neo4j connection functionality."""

    @classmethod
    def setup_class(cls):
        """Setup test class - runs once before all tests."""
        cls.test_node_label = "TestNode"
        logger.info("Starting Neo4j connection tests")

    @classmethod
    def teardown_class(cls):
        """Teardown test class - cleanup after all tests."""
        try:
            conn = get_connection()
            conn.execute_query(f"MATCH (n:{cls.test_node_label}) DETACH DELETE n")
            close_default_connection()
            logger.info("Test cleanup completed")
        except Exception as e:
            logger.warning(f"Cleanup error (non-critical): {e}")

    def setup_method(self, method):
        """Setup for each test method."""
        logger.info(f"Running test: {method.__name__}")
        try:
            conn = get_connection()
            conn.execute_query(f"MATCH (n:{self.test_node_label}) DETACH DELETE n")
        except Exception:
            pass

    def test_connection_initialization(self):
        """Test basic connection initialization."""
        conn = Neo4jConnection()

        assert conn.uri is not None
        assert conn.username == "neo4j"
        assert conn.password is not None
        assert conn.database == "neo4j"

        # Test that driver is not created until accessed
        assert conn._driver is None

        # Access driver to trigger lazy initialization
        driver = conn.driver
        assert driver is not None
        assert conn._driver is not None

        conn.close()

    def test_connectivity_verification(self):
        """Test connectivity verification."""
        conn = Neo4jConnection()

        # Should successfully connect and verify
        driver = conn.driver
        assert driver is not None

        # Test is_connected method
        assert conn.is_connected() is True

        # Close and verify disconnection
        conn.close()
        assert conn.is_connected() is False

    def test_execute_query(self):
        """Test basic query execution."""
        conn = get_connection()

        # Test simple query
        records, summary, keys = conn.execute_query(
            "RETURN 1 AS number, 'test' AS text"
        )

        assert len(records) == 1
        assert records[0]["number"] == 1
        assert records[0]["text"] == "test"
        assert "number" in keys
        assert "text" in keys

    def test_parameterized_query(self):
        """Test query execution with parameters."""
        conn = get_connection()

        parameters = {"name": "Test User", "age": 30, "active": True}

        query = """
        CREATE (n:TestNode {name: $name, age: $age, active: $active})
        RETURN n
        """

        records, _, _ = conn.execute_query(query, parameters)

        assert len(records) == 1
        node = records[0]["n"]
        assert node["name"] == "Test User"
        assert node["age"] == 30
        assert node["active"] is True

    def test_write_transaction(self):
        """Test write transaction execution."""
        conn = get_connection()

        def create_test_nodes(tx, count):
            result = tx.run(
                """
                UNWIND range(1, $count) AS id
                CREATE (n:TestNode {id: id, created_at: datetime()})
                RETURN count(n) AS nodes_created
                """,
                count=count,
            )
            return result.single()["nodes_created"]

        nodes_created = conn.execute_write_transaction(create_test_nodes, 5)
        assert nodes_created == 5

        # Verify nodes were created
        records, _, _ = conn.execute_query(
            "MATCH (n:TestNode) RETURN count(n) AS count"
        )
        assert records[0]["count"] == 5

    def test_read_transaction(self):
        """Test read transaction execution."""
        conn = get_connection()

        # First create some test data
        conn.execute_query(
            """
            CREATE (n1:TestNode {name: 'Node1'})
            CREATE (n2:TestNode {name: 'Node2'})
            CREATE (n3:TestNode {name: 'Node3'})
            """
        )

        def count_nodes(tx):
            result = tx.run("MATCH (n:TestNode) RETURN count(n) AS count")
            return result.single()["count"]

        count = conn.execute_read_transaction(count_nodes)
        assert count == 3

    def test_session_context_manager(self):
        """Test session context manager."""
        conn = get_connection()

        with conn.session() as session:
            # Create a node
            result = session.run(
                "CREATE (n:TestNode {name: $name}) RETURN n",
                name="Session Test",
            )
            node = result.single()["n"]
            assert node["name"] == "Session Test"

        # Verify node exists after session closes
        records, _, _ = conn.execute_query(
            "MATCH (n:TestNode {name: 'Session Test'}) RETURN n"
        )
        assert len(records) == 1

    def test_connection_context_manager(self):
        """Test connection context manager."""
        with Neo4jConnection() as conn:
            assert conn.is_connected() is True

            records, _, _ = conn.execute_query("RETURN 'connected' AS status")
            assert records[0]["status"] == "connected"

        # Connection should be closed after exiting context
        assert conn.is_connected() is False

    def test_batch_operations(self):
        """Test batch insert operations."""
        conn = get_connection()

        # Batch insert
        batch_data = [
            {"id": i, "name": f"Item {i}", "value": i * 10} for i in range(1, 51)
        ]

        query = """
        UNWIND $batch AS item
        CREATE (n:TestNode:BatchItem {
            id: item.id,
            name: item.name,
            value: item.value
        })
        RETURN count(n) AS created_count
        """

        records, _, _ = conn.execute_query(query, {"batch": batch_data})
        assert records[0]["created_count"] == 50

    def test_error_handling(self):
        """Test error handling for various scenarios."""
        # Test invalid query syntax
        conn = get_connection()
        with pytest.raises(ClientError):
            conn.execute_query("INVALID CYPHER SYNTAX")

        # Test querying non-existent labels returns empty results
        records, _, _ = conn.execute_query("MATCH (n:NonExistentLabel) RETURN n")
        assert len(records) == 0

    def test_connection_test_diagnostics(self):
        """Test the connection diagnostics method."""
        conn = get_connection()

        diagnostics = conn.test_connection()

        assert diagnostics["connected"] is True
        assert diagnostics["database_accessible"] is True
        assert diagnostics["error"] is None

        logger.info(f"Connection diagnostics: {diagnostics}")


def run_tests():
    """Run all tests and report results."""
    exit_code = pytest.main([__file__, "-v", "-s", "--tb=short"])

    if exit_code == 0:
        logger.info("✅ All tests passed successfully!")
    else:
        logger.error("❌ Some tests failed. Check the output above.")

    return exit_code


if __name__ == "__main__":
    # Simple demonstration / test
    print("Running Neo4j connection tests...\n")
    exit_code = run_tests()
    exit(exit_code)
