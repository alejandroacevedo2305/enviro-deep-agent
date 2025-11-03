"""LangChain tool for executing Cypher queries against Neo4j.

This module provides a LangChain-compatible tool that allows AI agents to query
the Neo4j knowledge graph using Cypher queries.

uv run -m tools.cypher_query_runner
"""

# %%
from __future__ import annotations

from typing import Any

from langchain_core.tools import StructuredTool

from Neo4j.retrievers.cypher_runner import run_cypher


def execute_cypher_query(cypher_query: str) -> list[dict[str, Any]]:
    """Execute a Cypher query against the Neo4j knowledge graph.

    This tool runs read-only Cypher queries to retrieve information from the
    environmental impact assessment documents knowledge graph.

    Graph Schema
    ------------
    Nodes:
    - Document: Environmental documents with content, filename, date, documentType
    - Project: Projects associated with documents
    - Region: Chilean regions where projects are located
    - Commune: Communes (municipalities) within regions
    - ProjectType: Types of projects (e.g., 'Centrales generadoras', mining)
    - Typology: Project typologies (codes: i1, i2, i3, i4, c, h1, etc.)
      * i1: Proyectos de desarrollo minero > 5.000 ton/mes
      * i2: Proyectos de exploración y prospección minera
      * i3: Instalaciones industriales o fabriles
      * i4: Proyectos de petróleo y gas
      * c: Centrales generadoras de energía
      * h1: Proyectos inmobiliarios y urbanísticos
    - Class: Document classifications (e.g., 'Flora', 'Fauna', 'Línea Base',
      'Adenda', 'ICSARA', 'PAS 146', 'Bosque Nativo', 'Avifauna')

    Relationships:
    - (Document)-[:BELONGS_TO]->(Project)
    - (Document)-[:IN_REGION]->(Region)
    - (Document)-[:IN_COMMUNE]->(Commune)
    - (Document)-[:HAS_PROJECT_TYPE]->(ProjectType)
    - (Document)-[:HAS_TIPOLOGIA]->(Typology)
    - (Document)-[:HAS_CLASS]->(Class)

    Query Guidelines
    ----------------
    1. **Always use LIMIT**: Prevent returning huge result sets
    2. **Use OPTIONAL MATCH**: For relationships that may not exist
    3. **Filter early**: Apply WHERE clauses as early as possible
    4. **Aggregate efficiently**: Use collect(DISTINCT ...) for lists
    5. **Content queries**: Use substring() for previews, full d.content only
       when needed

    Basic Query Patterns
    --------------------
    1. Count documents:
       MATCH (d:Document) RETURN count(d) AS total_documents

    2. Get document metadata with all context:
       MATCH (d:Document)
       OPTIONAL MATCH (d)-[:BELONGS_TO]->(p:Project)
       OPTIONAL MATCH (d)-[:IN_REGION]->(r:Region)
       OPTIONAL MATCH (d)-[:IN_COMMUNE]->(cm:Commune)
       OPTIONAL MATCH (d)-[:HAS_PROJECT_TYPE]->(pt:ProjectType)
       OPTIONAL MATCH (d)-[:HAS_TIPOLOGIA]->(t:Typology)
       OPTIONAL MATCH (d)-[:HAS_CLASS]->(c:Class)
       RETURN d.id AS doc_id, d.filename, p.name AS project,
              r.name AS region, cm.name AS commune, pt.name AS project_type,
              t.code AS typology, collect(DISTINCT c.name) AS classes
       LIMIT 10

    3. Filter by region:
       MATCH (d:Document)-[:IN_REGION]->(r:Region {name: 'Región de
       Antofagasta'})
       RETURN d.id, d.filename
       LIMIT 10

    4. Filter by typology (e.g., mining projects - i1):
       MATCH (d:Document)-[:HAS_TIPOLOGIA]->(t:Typology {code: 'i1'})
       RETURN d.id, d.filename
       LIMIT 10

    Advanced Query Patterns
    -----------------------
    5. Multiple class filtering (Flora AND Fauna):
       MATCH (d:Document)-[:HAS_CLASS]->(c1:Class)
       WHERE c1.name CONTAINS 'Flora'
       MATCH (d)-[:HAS_CLASS]->(c2:Class)
       WHERE c2.name CONTAINS 'Fauna'
       OPTIONAL MATCH (d)-[:BELONGS_TO]->(p:Project)
       OPTIONAL MATCH (d)-[:IN_REGION]->(r:Region)
       RETURN d.id, d.filename, p.name AS project, r.name AS region
       LIMIT 20

    6. Co-occurrence analysis (which classes appear together):
       MATCH (d:Document)-[:HAS_CLASS]->(c1:Class)
       MATCH (d)-[:HAS_CLASS]->(c2:Class)
       WHERE c1.name < c2.name
       RETURN c1.name AS class_a, c2.name AS class_b,
              count(DISTINCT d) AS together
       ORDER BY together DESC
       LIMIT 20

    7. Projects spanning multiple regions:
       MATCH (p:Project)<-[:BELONGS_TO]-(d:Document)-[:IN_REGION]->(r:Region)
       WITH p, collect(DISTINCT r.name) AS regions, count(DISTINCT d) AS
       num_docs
       WHERE size(regions) > 1
       RETURN p.name AS project, regions, num_docs
       ORDER BY size(regions) DESC, num_docs DESC
       LIMIT 15

    8. Projects spanning multiple communes:
       MATCH (p:Project)<-[:BELONGS_TO]-(d:Document)-[:IN_COMMUNE]->(cm:Commune)
       WITH p, collect(DISTINCT cm.name) AS communes, count(DISTINCT d) AS
       num_docs
       WHERE size(communes) > 1
       RETURN p.name AS project, size(communes) AS num_communes, num_docs
       ORDER BY num_communes DESC, num_docs DESC
       LIMIT 15

    9. Class diversity by project (projects with most unique classes):
       MATCH (p:Project)<-[:BELONGS_TO]-(d:Document)-[:HAS_CLASS]->(c:Class)
       WITH p, collect(DISTINCT c.name) AS classes, count(DISTINCT d) AS
       num_docs
       RETURN p.name AS project, size(classes) AS num_unique_classes, num_docs,
              classes[0..5] AS sample_classes
       ORDER BY num_unique_classes DESC
       LIMIT 15

    10. Regional analysis with cross-tabulation:
        MATCH (d:Document)-[:IN_REGION]->(r:Region)
        OPTIONAL MATCH (d)-[:HAS_TIPOLOGIA]->(t:Typology)
        RETURN r.name AS region, t.code AS typology, count(d) AS num_docs
        ORDER BY num_docs DESC
        LIMIT 20

    Content Extraction Patterns
    ---------------------------
    11. Extract full document content by ID:
        MATCH (d:Document {id: 'specific-doc-id'})
        RETURN d.id AS doc_id, d.filename, d.content AS page_content,
               d.documentType, d.date

    12. Content preview (first 500 chars) with metadata:
        MATCH (d:Document)-[:HAS_CLASS]->(c:Class {name: 'ICSARA'})
        OPTIONAL MATCH (d)-[:BELONGS_TO]->(p:Project)
        RETURN d.id, d.filename, substring(d.content, 0, 500) AS
        content_preview, p.name AS project
        LIMIT 10

    13. Search documents by content substring:
        MATCH (d:Document)
        WHERE d.content CONTAINS 'flora' OR d.content CONTAINS 'fauna'
        OPTIONAL MATCH (d)-[:BELONGS_TO]->(p:Project)
        OPTIONAL MATCH (d)-[:IN_REGION]->(r:Region)
        RETURN d.id, d.filename, substring(d.content, 0, 300) AS
        content_preview, p.name AS project, r.name AS region
        LIMIT 20

    14. Documents with longest content (size analysis):
        MATCH (d:Document)
        WHERE d.content IS NOT NULL
        OPTIONAL MATCH (d)-[:BELONGS_TO]->(p:Project)
        WITH d, p, size(d.content) AS content_length
        RETURN d.id, d.filename, content_length, p.name AS project
        ORDER BY content_length DESC
        LIMIT 10

    Temporal and Statistical Patterns
    ----------------------------------
    15. Recent documents (by date):
        MATCH (d:Document)
        WHERE d.date >= datetime('2025-10-01T00:00:00')
        OPTIONAL MATCH (d)-[:BELONGS_TO]->(p:Project)
        OPTIONAL MATCH (d)-[:IN_REGION]->(r:Region)
        RETURN d.id, d.filename, d.date AS created_date, p.name AS project,
               r.name AS region
        ORDER BY d.date DESC
        LIMIT 20

    16. Temporal distribution (monthly count):
        MATCH (d:Document)-[:HAS_CLASS]->(c:Class {name: 'Adenda'})
        WHERE d.date >= datetime('2025-01-01T00:00:00')
          AND d.date < datetime('2026-01-01T00:00:00')
        WITH date.truncate('month', d.date) AS month, count(d) AS num_docs
        RETURN toString(month) AS mes, num_docs
        ORDER BY month

    17. Average documents per project by region:
        MATCH (d:Document)-[:BELONGS_TO]->(p:Project)
        MATCH (d)-[:IN_REGION]->(r:Region)
        WITH r, p, count(d) AS docs_in_project
        RETURN r.name AS region, count(DISTINCT p) AS num_projects,
               avg(docs_in_project) AS avg_docs_per_project,
               max(docs_in_project) AS max_docs_per_project
        ORDER BY avg_docs_per_project DESC

    Specialized Analysis Patterns
    ------------------------------
    18. ICSARA and Adenda comparison by project:
        MATCH (p:Project)<-[:BELONGS_TO]-(d:Document)
        OPTIONAL MATCH (d)-[:HAS_CLASS]->(c1:Class {name: 'ICSARA'})
        OPTIONAL MATCH (d)-[:HAS_CLASS]->(c2:Class {name: 'Adenda'})
        WITH p,
             count(DISTINCT CASE WHEN c1 IS NOT NULL THEN d END) AS
             icsara_count,
             count(DISTINCT CASE WHEN c2 IS NOT NULL THEN d END) AS
             adenda_count
        WHERE icsara_count > 0 OR adenda_count > 0
        RETURN p.name AS project, icsara_count, adenda_count,
               icsara_count + adenda_count AS total
        ORDER BY total DESC
        LIMIT 20

    19. Find rare class combinations (< 10 co-occurrences):
        MATCH (d:Document)-[:HAS_CLASS]->(c1:Class)
        MATCH (d)-[:HAS_CLASS]->(c2:Class)
        WHERE c1.name < c2.name
        WITH c1.name AS class_a, c2.name AS class_b, count(DISTINCT d) AS
        together
        WHERE together < 10 AND together > 1
        RETURN class_a, class_b, together
        ORDER BY together DESC
        LIMIT 20

    20. Classes exclusive to mining projects (i1, i2, i3):
        MATCH (d_mining:Document)-[:HAS_TIPOLOGIA]->(t:Typology)
        WHERE t.code IN ['i1', 'i2', 'i3']
        MATCH (d_mining)-[:HAS_CLASS]->(c:Class)
        WITH c, count(DISTINCT d_mining) AS mining_count
        MATCH (d_all:Document)-[:HAS_CLASS]->(c)
        WITH c, mining_count, count(d_all) AS total_count
        WHERE mining_count = total_count AND total_count > 5
        RETURN c.name AS class_name, mining_count
        ORDER BY mining_count DESC
        LIMIT 15

    Listing and Discovery Patterns
    -------------------------------
    21. List all available regions:
        MATCH (r:Region)
        RETURN r.name AS region
        ORDER BY r.name

    22. List communes by region with document counts:
        MATCH (d:Document)-[:IN_REGION]->(r:Region)
        MATCH (d)-[:IN_COMMUNE]->(cm:Commune)
        WITH r, collect(DISTINCT cm.name) AS comunas, count(DISTINCT cm) AS
        num_comunas
        RETURN r.name AS region, num_comunas, comunas
        ORDER BY num_comunas DESC

    23. List all classes with usage statistics:
        MATCH (c:Class)
        OPTIONAL MATCH (c)<-[:HAS_CLASS]-(d:Document)
        RETURN c.name AS class, count(d) AS total_documentos,
               CASE
                 WHEN count(d) = 0 THEN 'Sin documentos'
                 WHEN count(d) < 10 THEN 'Bajo uso'
                 WHEN count(d) < 100 THEN 'Uso medio'
                 WHEN count(d) < 1000 THEN 'Uso alto'
                 ELSE 'Uso muy alto'
               END AS categoria_uso
        ORDER BY total_documentos DESC

    24. Show all relationship types in database:
        CALL db.relationshipTypes() YIELD relationshipType
        RETURN relationshipType
        ORDER BY relationshipType

    25. Count nodes by label:
        CALL db.labels() YIELD label
        CALL {
          WITH label
          MATCH (n)
          WHERE label IN labels(n)
          RETURN count(n) AS count
        }
        RETURN label, count
        ORDER BY count DESC

    Parameters
    ----------
    cypher_query:
        A valid Cypher query string to execute. Should be a read-only query
        (MATCH, RETURN, WITH, WHERE, ORDER BY, LIMIT, etc.). Write operations
        are not supported.

    Returns
    -------
    list[dict[str, Any]]
        List of result records as dictionaries, where keys are the column names
        specified in the RETURN clause of the Cypher query.

    Examples
    --------
    Query all regions:
    >>> execute_cypher_query("MATCH (r:Region) RETURN r.name AS region LIMIT 5")
    [{'region': 'Región de Antofagasta'}, {'region': 'Región Metropolitana'}, ...]

    Count documents by project type:
    >>> execute_cypher_query(
    ...     "MATCH (d:Document)-[:HAS_PROJECT_TYPE]->(pt:ProjectType) "
    ...     "RETURN pt.name AS type, count(d) AS num_docs "
    ...     "ORDER BY num_docs DESC LIMIT 5"
    ... )
    [{'type': 'Centrales generadoras', 'num_docs': 150}, ...]

    Find Flora and Fauna documents in Antofagasta:
    >>> execute_cypher_query(
    ...     "MATCH (d:Document)-[:HAS_CLASS]->(c1:Class) "
    ...     "WHERE c1.name CONTAINS 'Flora' "
    ...     "MATCH (d)-[:HAS_CLASS]->(c2:Class) "
    ...     "WHERE c2.name CONTAINS 'Fauna' "
    ...     "MATCH (d)-[:IN_REGION]->(r:Region {name: 'Región de Antofagasta'}) "
    ...     "RETURN d.id, d.filename LIMIT 10"
    ... )
    [{'d.id': 'doc-123', 'd.filename': 'flora_fauna_study.pdf'}, ...]
    """
    return run_cypher(cypher_query)


# Create the LangChain tool
cypher_query_tool = StructuredTool.from_function(
    func=execute_cypher_query,
    name="cypher_query_runner",
    description=(
        "Execute read-only Cypher queries against the Neo4j knowledge graph "
        "containing environmental impact assessment documents from Chile. "
        "Use this tool for: (1) Structured analysis: counts, aggregations, "
        "filtering by region/commune/typology/class, (2) Document discovery: "
        "find document IDs and metadata, (3) Content extraction: retrieve full "
        "document content using 'd.content' for detailed analysis. "
        "IMPORTANT: You can extract d.content (full text) from documents to "
        "analyze their contents, identify patterns, extract questions from "
        "evaluators (ICSARA), or find specific information. Use LIMIT 5-10 when "
        "extracting full content to avoid overwhelming results. "
        "Returns raw query results as a list of dictionaries."
    ),
)


if __name__ == "__main__":
    # Simple demonstration of the tool
    print("🔧 Testing Cypher Query Tool\n")

    # Test 1: Count documents
    print("📌 Test 1: Count all documents")
    result = cypher_query_tool.invoke(
        {"cypher_query": "MATCH (d:Document) RETURN count(d) AS total"}
    )
    print(f"→ Result: {result}\n")

    # Test 2: List regions
    print("📌 Test 2: List all regions")
    result = cypher_query_tool.invoke(
        {
            "cypher_query": "MATCH (r:Region) RETURN r.name AS region ORDER BY r.name LIMIT 5"
        }
    )
    print(f"→ Result: {result}\n")

    # Test 3: Documents by project type
    print("📌 Test 3: Documents by project type (top 3)")
    result = cypher_query_tool.invoke(
        {
            "cypher_query": (
                "MATCH (d:Document)-[:HAS_PROJECT_TYPE]->(pt:ProjectType) "
                "RETURN pt.name AS project_type, count(d) AS num_docs "
                "ORDER BY num_docs DESC LIMIT 3"
            )
        }
    )
    print(f"→ Result: {result}\n")

    # Test 4: Top classes
    print("📌 Test 4: Top 5 document classes by frequency")
    result = cypher_query_tool.invoke(
        {
            "cypher_query": (
                "MATCH (:Document)-[:HAS_CLASS]->(c:Class) "
                "RETURN c.name AS class, count(*) AS freq "
                "ORDER BY freq DESC LIMIT 5"
            )
        }
    )
    print(f"→ Result: {result}\n")

    print("✅ All tests completed successfully!")
