"""Connection module for Neo4j AWS Hosted Database.

Simple and straightforward Neo4j connection with retry logic.
"""

# %%
import logging
import os
import time
from contextlib import contextmanager
from functools import wraps

from dotenv import load_dotenv
from neo4j import Driver, GraphDatabase
from neo4j.exceptions import (
    AuthError,
    Neo4jError,
    ServiceUnavailable,
    TransientError,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv(override=True)


class Neo4jConnection:
    """Manages connection to Neo4j database with retry logic."""

    def __init__(
        self,
        uri: str | None = None,
        username: str | None = None,
        password: str | None = None,
        database: str = "neo4j",
        max_retry_attempts: int = 3,
        retry_delay: float = 1.0,
    ):
        """Initialize Neo4j connection manager.

        Args:
            uri: Neo4j connection URI. Defaults to environment variable.
            username: Neo4j username. Defaults to environment variable.
            password: Neo4j password. Defaults to environment variable.
            database: Target database name. Defaults to "neo4j".
            max_retry_attempts: Maximum retry attempts for transient errors.
            retry_delay: Delay between retry attempts in seconds.
        """
        # Connection parameters with fallback to environment variables
        self.uri = uri or self._get_uri_from_env()
        self.username = username or os.getenv("NEO4J_USERNAME", "neo4j")
        self.password = password or os.getenv("NEO4J_PASSWORD")
        self.database = database

        # Retry configuration
        self.max_retry_attempts = max_retry_attempts
        self.retry_delay = retry_delay

        # Driver instance (lazy initialization)
        self._driver: Driver | None = None

        # Validate credentials
        if not self.password:
            msg = (
                "Neo4j password not provided. Set NEO4J_PASSWORD environment variable."
            )
            raise ValueError(msg)

    def _get_uri_from_env(self) -> str:
        """Get Neo4j URI from environment or use default."""
        env_uri = os.getenv("NEO4J_URI", "")
        if env_uri:
            return env_uri
        # Default to NVIRO hosted Neo4j
        return "neo4j+s://neo4j-community.nviro.cl:7687"

    def retry_on_transient_error(self, func):
        """Decorator to retry operations on transient errors."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(self.max_retry_attempts):
                try:
                    return func(*args, **kwargs)
                except (ServiceUnavailable, TransientError) as e:
                    last_error = e
                    if attempt < self.max_retry_attempts - 1:
                        logger.warning(
                            f"Transient error on attempt "
                            f"{attempt + 1}/{self.max_retry_attempts}: {e}. "
                            f"Retrying in {self.retry_delay} seconds..."
                        )
                        time.sleep(self.retry_delay * (attempt + 1))
                    else:
                        logger.error(f"Max retry attempts reached. Error: {e}")
                        raise
            raise last_error

        return wrapper

    @property
    def driver(self) -> Driver:
        """Get or create the Neo4j driver instance."""
        if self._driver is None:
            self._driver = self._create_driver()
        return self._driver

    def _create_driver(self) -> Driver:
        """Create a new Neo4j driver instance."""
        logger.info(f"Creating Neo4j driver for {self.uri}")

        try:
            driver = GraphDatabase.driver(
                self.uri,
                auth=(self.username, self.password),
                max_connection_lifetime=3600,
                max_connection_pool_size=50,
                connection_acquisition_timeout=60.0,
            )

            # Verify connectivity
            driver.verify_connectivity()
            logger.info("Successfully connected to Neo4j")

            return driver

        except AuthError as e:
            logger.error(f"Authentication failed: {e}")
            raise
        except ServiceUnavailable as e:
            logger.error(f"Neo4j service unavailable at {self.uri}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error creating driver: {e}")
            raise

    def connect(self) -> Driver:
        """Establish connection to Neo4j database."""
        return self.driver

    def close(self) -> None:
        """Close the Neo4j driver connection."""
        if self._driver:
            self._driver.close()
            self._driver = None
            logger.info("Neo4j driver connection closed")

    def is_connected(self) -> bool:
        """Check if the driver is connected and responsive."""
        if not self._driver:
            return False

        try:
            self._driver.verify_connectivity()
            return True
        except (ServiceUnavailable, Neo4jError):
            return False

    @contextmanager
    def session(self, **session_config):
        """Context manager for Neo4j sessions with automatic cleanup.

        Args:
            **session_config: Additional session configuration parameters.

        Yields:
            Neo4j Session object.
        """
        session = self.driver.session(database=self.database, **session_config)
        try:
            yield session
        finally:
            session.close()

    def execute_query(self, query: str, parameters: dict | None = None, **kwargs):
        """Execute a Cypher query with retry logic.

        Args:
            query: Cypher query string.
            parameters: Query parameters.
            **kwargs: Additional query execution parameters.

        Returns:
            Tuple of (records, summary, keys).
        """

        @self.retry_on_transient_error
        def _execute():
            return self.driver.execute_query(
                query, parameters or {}, database_=self.database, **kwargs
            )

        return _execute()

    def execute_write_transaction(self, transaction_func, *args, **kwargs):
        """Execute a write transaction with retry logic.

        Args:
            transaction_func: Function to execute within transaction.
            *args, **kwargs: Arguments to pass to transaction function.

        Returns:
            Result from transaction function.
        """

        @self.retry_on_transient_error
        def _execute():
            with self.session() as session:
                return session.execute_write(transaction_func, *args, **kwargs)

        return _execute()

    def execute_read_transaction(self, transaction_func, *args, **kwargs):
        """Execute a read transaction with retry logic.

        Args:
            transaction_func: Function to execute within transaction.
            *args, **kwargs: Arguments to pass to transaction function.

        Returns:
            Result from transaction function.
        """

        @self.retry_on_transient_error
        def _execute():
            with self.session() as session:
                return session.execute_read(transaction_func, *args, **kwargs)

        return _execute()

    def test_connection(self) -> dict:
        """Test the database connection and return diagnostic information."""
        results = {
            "uri": self.uri,
            "database": self.database,
            "connected": False,
            "error": None,
        }

        try:
            # Test basic connectivity
            self.driver.verify_connectivity()
            results["connected"] = True

            # Test database accessibility
            records, _, _ = self.execute_query("RETURN 1 AS test")
            results["database_accessible"] = len(records) > 0

            logger.info(f"Connection test successful: {results}")

        except Exception as e:
            results["error"] = str(e)
            logger.error(f"Connection test failed: {e}")

        return results

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# Singleton instance for convenience
_default_connection: Neo4jConnection | None = None


def get_connection() -> Neo4jConnection:
    """Get or create the default Neo4j connection instance."""
    global _default_connection
    if _default_connection is None:
        _default_connection = Neo4jConnection()
    return _default_connection


def close_default_connection() -> None:
    """Close the default connection if it exists."""
    global _default_connection
    if _default_connection:
        _default_connection.close()
        _default_connection = None


if __name__ == "__main__":
    # Simple demonstration
    print("Testing Neo4j connection...")

    # Test with context manager
    with Neo4jConnection() as conn:
        diagnostics = conn.test_connection()
        print(f"Connection diagnostics: {diagnostics}")

        # Simple query test
        if diagnostics["connected"]:
            records, _, _ = conn.execute_query("RETURN 'Hello Neo4j!' AS message")
            print(f"Query result: {records[0]['message']}")
