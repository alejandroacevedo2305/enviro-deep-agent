"""Knowledge Graph Database setup for hybrid search with Neo4j.

This module creates and manages a Neo4j knowledge graph that combines
vector embeddings with graph relationships for powerful hybrid search.
"""

# %%
from __future__ import annotations

import logging
import os

# Add parent directory to path for imports
import sys
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain_community.graphs import Neo4jGraph
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from neo4j.exceptions import Neo4jError

sys.path.append(str(Path(__file__).parent.parent))

from connection.conn import Neo4jConnection

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv(override=True)


class KnowledgeGraphDB:
    """Manages a Neo4j knowledge graph for document storage and hybrid search."""

    def __init__(
        self,
        connection: Neo4jConnection | None = None,
        embedding_model: str = "text-embedding-3-large",
        llm_model: str = "gpt-4o-mini",
    ):
        """Initialize the Knowledge Graph Database.

        Args:
            connection: Neo4j connection instance. Creates new if None.
            embedding_model: OpenAI embedding model to use.
            llm_model: OpenAI chat model to use.
        """
        # Set up Neo4j connection
        self.connection = connection or Neo4jConnection()

        # Set up OpenAI models
        self.embeddings = OpenAIEmbeddings(
            model=embedding_model,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )

        self.llm = ChatOpenAI(
            model=llm_model,
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )

        # Initialize LangChain Neo4j graph
        self.graph = Neo4jGraph(
            url=self.connection.uri,
            username=self.connection.username,
            password=self.connection.password,
            database=self.connection.database,
        )

        logger.info(
            f"Initialized KnowledgeGraphDB with {embedding_model} and {llm_model}"
        )

    def initialize_empty_graph(self) -> None:
        """Create an empty knowledge graph with proper constraints and indexes."""
        logger.info("Initializing empty knowledge graph...")

        try:
            # Clear existing data (optional - comment out if you want to keep data)
            self._clear_graph()

            # Create constraints for unique identifiers
            self._create_constraints()

            # Create indexes for better query performance
            self._create_indexes()

            # Create vector index for embeddings
            self._create_vector_index()

            logger.info("Empty knowledge graph initialized successfully")

        except Neo4jError as e:
            logger.error(f"Failed to initialize graph: {e}")
            raise

    def _clear_graph(self) -> None:
        """Clear all nodes and relationships from the graph."""
        query = "MATCH (n) DETACH DELETE n"
        self.connection.execute_query(query)
        logger.info("Cleared existing graph data")

    def _create_constraints(self) -> None:
        """Create uniqueness constraints for the graph."""
        constraints = [
            # Constraint for Document nodes
            (
                "CREATE CONSTRAINT document_id IF NOT EXISTS "
                "FOR (d:Document) REQUIRE d.id IS UNIQUE"
            ),
            # Constraint for Project nodes
            (
                "CREATE CONSTRAINT project_name IF NOT EXISTS "
                "FOR (p:Project) REQUIRE p.name IS UNIQUE"
            ),
            # Constraint for Class nodes (Flora, Fauna, etc.)
            (
                "CREATE CONSTRAINT class_name IF NOT EXISTS "
                "FOR (c:Class) REQUIRE c.name IS UNIQUE"
            ),
            # Constraint for Region nodes
            (
                "CREATE CONSTRAINT region_name IF NOT EXISTS "
                "FOR (r:Region) REQUIRE r.name IS UNIQUE"
            ),
            # Constraint for Commune nodes
            (
                "CREATE CONSTRAINT commune_name IF NOT EXISTS "
                "FOR (cm:Commune) REQUIRE cm.name IS UNIQUE"
            ),
            # Constraint for ProjectType nodes
            (
                "CREATE CONSTRAINT project_type_name IF NOT EXISTS "
                "FOR (pt:ProjectType) REQUIRE pt.name IS UNIQUE"
            ),
            # Constraint for Typology nodes
            (
                "CREATE CONSTRAINT typology_code IF NOT EXISTS "
                "FOR (t:Typology) REQUIRE t.code IS UNIQUE"
            ),
        ]

        for constraint in constraints:
            try:
                self.connection.execute_query(constraint)
                logger.info(f"Created constraint: {constraint.split('CONSTRAINT')[1]}")
            except Neo4jError as e:
                if "already exists" in str(e).lower():
                    logger.debug(f"Constraint already exists: {e}")
                else:
                    raise

    def _create_indexes(self) -> None:
        """Create indexes for better query performance."""
        indexes = [
            # Index for Document properties
            "CREATE INDEX document_filename IF NOT EXISTS FOR (d:Document) ON (d.filename)",
            "CREATE INDEX document_type IF NOT EXISTS FOR (d:Document) ON (d.documentType)",
            "CREATE INDEX document_date IF NOT EXISTS FOR (d:Document) ON (d.date)",
            # Index for full-text search on content
            (
                "CREATE FULLTEXT INDEX document_content IF NOT EXISTS "
                "FOR (d:Document) ON EACH [d.content, d.summary]"
            ),
        ]

        for index in indexes:
            try:
                self.connection.execute_query(index)
                logger.info(f"Created index: {index.split('INDEX')[1]}")
            except Neo4jError as e:
                if "already exists" in str(e).lower():
                    logger.debug(f"Index already exists: {e}")
                else:
                    raise

    def _create_vector_index(self) -> None:
        """Create vector index for similarity search."""
        # Drop existing vector index if it exists
        try:
            self.connection.execute_query("DROP INDEX document_embeddings IF EXISTS")
        except Neo4jError:
            pass  # Index doesn't exist, which is fine

        # Create new vector index for embeddings
        vector_index_query = """
        CREATE VECTOR INDEX document_embeddings IF NOT EXISTS
        FOR (d:Document) ON d.embedding
        OPTIONS {
            indexConfig: {
                `vector.dimensions`: 3072,
                `vector.similarity_function`: 'cosine'
            }
        }
        """

        try:
            self.connection.execute_query(vector_index_query)
            logger.info("Created vector index for document embeddings")
        except Neo4jError as e:
            logger.error(f"Failed to create vector index: {e}")
            # Try with default dimensions if 3072 fails
            fallback_query = """
            CREATE VECTOR INDEX document_embeddings IF NOT EXISTS
            FOR (d:Document) ON d.embedding
            OPTIONS {
                indexConfig: {
                    `vector.dimensions`: 1536,
                    `vector.similarity_function`: 'cosine'
                }
            }
            """
            self.connection.execute_query(fallback_query)
            logger.info("Created vector index with default dimensions (1536)")

    def add_document(self, document: Document) -> str:
        """Add a single document to the knowledge graph.

        Args:
            document: LangChain Document object with content and metadata

        Returns:
            Document ID in the graph
        """
        # Generate embedding for the document
        embedding = self.embeddings.embed_documents([document.page_content])[0]

        # Extract metadata
        metadata = document.metadata
        # Try to get file_id from fileIdentifier or extract from filename
        doc_id = metadata.get("fileIdentifier", "")
        if not doc_id:
            # Extract from filename pattern: NNNN-type-file_id_XXX.json
            filename = metadata.get("fileName", "")
            if "file_id_" in filename:
                doc_id = filename.split("file_id_")[1].split(".")[0]
            else:
                doc_id = filename

        filename = metadata.get("fileName", "")
        project_name = metadata.get("seaProjectName", "")
        region = metadata.get("seaProjectRegion", "")
        commune = metadata.get("seaProjectEiDocumentCommunes", "")
        project_type = metadata.get("seaProjectProjectType", "")
        typology = metadata.get("seaProjectTypology", "")
        classes = metadata.get("classes", [])

        # Create Document node with embedding
        doc_query = """
        MERGE (d:Document {id: $doc_id})
        SET d.content = $content,
            d.filename = $filename,
            d.documentType = $doc_type,
            d.embedding = $embedding,
            d.projectName = $project_name,
            d.date = datetime()
        RETURN d.id as doc_id
        """

        self.connection.execute_query(
            doc_query,
            {
                "doc_id": doc_id,
                "content": document.page_content[:10000],  # Limit content size
                "filename": filename,
                "doc_type": metadata.get("documentType", ""),
                "project_name": project_name,
                "embedding": embedding,
            },
        )

        # Create relationships to Project
        if project_name:
            project_query = """
            MERGE (p:Project {name: $project_name})
            WITH p
            MATCH (d:Document {id: $doc_id})
            MERGE (d)-[:BELONGS_TO]->(p)
            """
            self.connection.execute_query(
                project_query, {"project_name": project_name, "doc_id": doc_id}
            )

        # Create relationships to Region
        if region:
            region_query = """
            MERGE (r:Region {name: $region})
            WITH r
            MATCH (d:Document {id: $doc_id})
            MERGE (d)-[:IN_REGION]->(r)
            """
            self.connection.execute_query(
                region_query, {"region": region, "doc_id": doc_id}
            )

        # Create relationships to Commune
        if commune:
            commune_query = """
            MERGE (cm:Commune {name: $commune})
            WITH cm
            MATCH (d:Document {id: $doc_id})
            MERGE (d)-[:IN_COMMUNE]->(cm)
            """
            self.connection.execute_query(
                commune_query, {"commune": commune, "doc_id": doc_id}
            )

        # Create relationships to ProjectType
        if project_type:
            project_type_query = """
            MERGE (pt:ProjectType {name: $project_type})
            WITH pt
            MATCH (d:Document {id: $doc_id})
            MERGE (d)-[:HAS_PROJECT_TYPE]->(pt)
            """
            self.connection.execute_query(
                project_type_query, {"project_type": project_type, "doc_id": doc_id}
            )

        # Create relationships to Typology
        if typology:
            typology_query = """
            MERGE (t:Typology {code: $typology})
            WITH t
            MATCH (d:Document {id: $doc_id})
            MERGE (d)-[:HAS_TIPOLOGIA]->(t)
            """
            self.connection.execute_query(
                typology_query, {"typology": typology, "doc_id": doc_id}
            )

        # Create relationships to Classes
        for class_info in classes:
            if isinstance(class_info, dict):
                class_name = class_info.get("class", "")
                if class_name:
                    class_query = """
                    MERGE (c:Class {name: $class_name})
                    WITH c
                    MATCH (d:Document {id: $doc_id})
                    MERGE (d)-[:HAS_CLASS]->(c)
                    """
                    self.connection.execute_query(
                        class_query, {"class_name": class_name, "doc_id": doc_id}
                    )

        logger.info(f"Added document {doc_id} to knowledge graph")
        return doc_id

    def add_documents_batch(
        self, documents: list[Document], batch_size: int = 100
    ) -> None:
        """Add multiple documents to the knowledge graph in batches.

        Args:
            documents: List of LangChain Document objects
            batch_size: Number of documents to process at once
        """
        total = len(documents)
        logger.info(f"Adding {total} documents to knowledge graph...")

        for i in range(0, total, batch_size):
            batch = documents[i : i + batch_size]
            for doc in batch:
                try:
                    self.add_document(doc)
                except Exception as e:
                    logger.error(f"Failed to add document: {e}")

            processed = min(i + batch_size, total)
            logger.info(f"Processed {processed}/{total} documents")

    def hybrid_search(
        self, query: str, top_k: int = 5, similarity_threshold: float = 0.7
    ) -> list[dict[str, Any]]:
        """Perform hybrid search combining vector similarity and graph traversal.

        Args:
            query: Search query text
            top_k: Number of results to return
            similarity_threshold: Minimum similarity score

        Returns:
            List of search results with documents and metadata
        """
        # Generate embedding for query
        query_embedding = self.embeddings.embed_query(query)

        # Hybrid search query combining vector similarity and graph relationships
        search_query = """
        // Vector similarity search
        CALL db.index.vector.queryNodes('document_embeddings', $top_k, $query_embedding)
        YIELD node as doc, score
        WHERE score >= $threshold

        // Enrich with graph relationships
        OPTIONAL MATCH (doc)-[:BELONGS_TO]->(p:Project)
        OPTIONAL MATCH (doc)-[:IN_REGION]->(r:Region)
        OPTIONAL MATCH (doc)-[:IN_COMMUNE]->(cm:Commune)
        OPTIONAL MATCH (doc)-[:HAS_PROJECT_TYPE]->(pt:ProjectType)
        OPTIONAL MATCH (doc)-[:HAS_TIPOLOGIA]->(t:Typology)
        OPTIONAL MATCH (doc)-[:HAS_CLASS]->(c:Class)

        RETURN doc.id as doc_id,
               doc.filename as filename,
               doc.content as content,
               score,
               p.name as project,
               r.name as region,
               cm.name as commune,
               pt.name as project_type,
               t.code as typology,
               collect(DISTINCT c.name) as classes
        ORDER BY score DESC
        LIMIT $top_k
        """

        try:
            records, _, _ = self.connection.execute_query(
                search_query,
                {
                    "query_embedding": query_embedding,
                    "top_k": top_k,
                    "threshold": similarity_threshold,
                },
            )

            results = []
            for record in records:
                results.append(
                    {
                        "doc_id": record["doc_id"],
                        "filename": record["filename"],
                        "content": record["content"],
                        "score": record["score"],
                        "project": record["project"],
                        "region": record["region"],
                        "commune": record["commune"],
                        "project_type": record["project_type"],
                        "typology": record["typology"],
                        "classes": record["classes"],
                    }
                )

            return results

        except Neo4jError as e:
            logger.error(f"Hybrid search failed: {e}")
            return []

    def get_graph_statistics(self) -> dict[str, Any]:
        """Get statistics about the knowledge graph."""
        stats_query = """
        OPTIONAL MATCH (d:Document)
        WITH count(d) as total_docs
        OPTIONAL MATCH (p:Project)
        WITH total_docs, count(p) as total_projects
        OPTIONAL MATCH (r:Region)
        WITH total_docs, total_projects, count(r) as total_regions
        OPTIONAL MATCH (cm:Commune)
        WITH total_docs, total_projects, total_regions, count(cm) as total_communes
        OPTIONAL MATCH (pt:ProjectType)
        WITH total_docs, total_projects, total_regions, total_communes, count(pt) as total_project_types
        OPTIONAL MATCH (t:Typology)
        WITH total_docs, total_projects, total_regions, total_communes, total_project_types, count(t) as total_typologies
        OPTIONAL MATCH (c:Class)
        RETURN total_docs, total_projects, total_regions, total_communes,
               total_project_types, total_typologies, count(c) as total_classes
        """

        try:
            records, _, _ = self.connection.execute_query(stats_query)
            if records:
                return dict(records[0])
            return {
                "total_docs": 0,
                "total_projects": 0,
                "total_regions": 0,
                "total_communes": 0,
                "total_project_types": 0,
                "total_typologies": 0,
                "total_classes": 0,
            }
        except Neo4jError:
            return {
                "total_docs": 0,
                "total_projects": 0,
                "total_regions": 0,
                "total_communes": 0,
                "total_project_types": 0,
                "total_typologies": 0,
                "total_classes": 0,
            }

    def close(self) -> None:
        """Close the connection to Neo4j."""
        self.connection.close()


if __name__ == "__main__":
    # Simple demonstration / test
    print("=" * 80)
    print("Knowledge Graph Database Setup")
    print("=" * 80)

    # Initialize the knowledge graph
    kg = KnowledgeGraphDB()

    # Create empty graph with proper structure
    kg.initialize_empty_graph()

    # Get statistics
    stats = kg.get_graph_statistics()
    print("\nGraph Statistics:")
    print(f"  Documents: {stats['total_docs']}")
    print(f"  Projects: {stats['total_projects']}")
    print(f"  Regions: {stats['total_regions']}")
    print(f"  Communes: {stats['total_communes']}")
    print(f"  Project Types: {stats['total_project_types']}")
    print(f"  Typologies: {stats['total_typologies']}")
    print(f"  Classes: {stats['total_classes']}")

    print("\n✓ Empty knowledge graph created successfully!")
    print("✓ Ready to ingest documents from documents_to_upsert/")

    # Clean up
    kg.close()
