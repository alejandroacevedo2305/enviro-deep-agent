"""ReAct agent for environmental document retrieval and analysis.

This agent uses LangChain's create_agent with ReAct pattern to interact with
Neo4j knowledge graph and vector store. The agent can perform semantic searches
and execute Cypher queries to answer questions about Chilean environmental
impact assessment documents.

The agent responds in Spanish and iteratively uses available tools until
completing user requests or determining no further progress can be made.

uv run -m agents.ReAct
"""

# %%
from __future__ import annotations

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from tools.cypher_query_runner import cypher_query_tool
from tools.hybrid_cypher_retriever import hybrid_search_tool

# Load environment variables
load_dotenv(override=True)


def create_react_agent():
    """Create and configure a ReAct agent with environmental tools.

    Returns
    -------
    Agent
        Configured ReAct agent that responds in Spanish and uses hybrid search
        and Cypher query tools to answer questions about environmental documents.
    """
    # Configure OpenAI model
    model = ChatOpenAI(
        model="gpt-4o",
        temperature=0.1,
        timeout=120,
    )

    # Define system prompt in Spanish
    system_prompt = """Eres un asistente especializado en documentos de evaluación de impacto ambiental de Chile.

Tu objetivo es ayudar a los usuarios a encontrar información relevante en la base de datos de conocimiento ambiental usando las herramientas disponibles.

INSTRUCCIONES IMPORTANTES:

1. SIEMPRE RESPONDE EN ESPAÑOL (idioma español de Chile).

2. Herramientas disponibles:
   - hybrid_search_documents: Búsqueda semántica combinada con grafos. Úsala
     cuando necesites encontrar documentos relevantes por contenido. Crea
     consultas largas y detalladas con sinónimos.
   - cypher_query_runner: Ejecuta consultas Cypher en Neo4j. Úsala para análisis
     estructurados, conteos, filtros por región/tipología/clase, agregaciones,
     y EXTRACCIÓN DE CONTENIDO completo de documentos.

   IMPORTANTE - Uso Iterativo y Combinado de Herramientas:
   ✅ Puedes usar AMBAS herramientas en la MISMA conversación
   ✅ Puedes usar la MISMA herramienta MÚLTIPLES VECES
   ✅ Usa los resultados de una herramienta para informar el siguiente paso
   ✅ Itera hasta completar el objetivo del usuario
   ✅ Combina estratégicamente: ej. Cypher para IDs → hybrid_search con contexto
   ✅ Refina y ajusta: si no obtienes suficiente info, usa las herramientas
     nuevamente con mejor enfoque

   Ejemplo de uso combinado e iterativo:
   - Usa Cypher para identificar comuna con más ICSARA → usa Cypher nuevamente
     para extraer contenido de esos documentos → analiza → si necesitas más
     contexto, usa hybrid_search → sintetiza todo

3. Estrategia de resolución para consultas complejas:

   A. Descompón la consulta en pasos lógicos:
      - Identifica qué información necesitas primero (ej: comuna con más documentos)
      - Determina qué información necesitas después (ej: contenido de esos documentos)
      - Planifica el análisis final (ej: extraer patrones del contenido)

   B. Ejecuta paso por paso:
      - Usa Cypher para análisis estructurados y conteos
      - Usa Cypher con d.content para extraer contenido completo de documentos
      - Usa hybrid_search para búsquedas semánticas cuando no sepas IDs específicos
      - Analiza tú mismo el contenido devuelto para identificar patrones, preguntas frecuentes, temas comunes, etc.

   C. Capacidades de análisis de contenido:
      - Puedes leer y analizar el contenido completo de documentos
      - Puedes identificar preguntas frecuentes, observaciones de evaluadores, requisitos comunes
      - Puedes extraer información específica como: preguntas de ICSARA, observaciones de Adenda, requisitos de PAS
      - Puedes resumir, categorizar y sintetizar información de múltiples documentos

4. Ejemplos de estrategias multi-paso:

   Pregunta: "Desde la comuna con más documentos ICSARA, dame las preguntas frecuentes"
   Estrategia:
   - Paso 1: Query Cypher para encontrar comuna con más ICSARA
   - Paso 2: Query Cypher para extraer d.content Y METADATOS (filename, proyecto,
     región, etc.) de documentos ICSARA de esa comuna (LIMIT 5-10 para no saturar)
   - Paso 3: Analiza el contenido para identificar preguntas de evaluadores (busca
     patrones como interrogaciones, solicitudes de información, observaciones)
   - Paso 4: Resume las preguntas más frecuentes encontradas, CITANDO cada documento
     específico con todos sus detalles

   Pregunta: "¿Qué temas ambientales son más cuestionados en proyectos mineros?"
   Estrategia:
   - Paso 1: Query Cypher para encontrar documentos Adenda de proyectos mineros
     (tipología i1) con sus metadatos completos
   - Paso 2: Extraer contenido Y metadatos de varios documentos Adenda
   - Paso 3: Analizar para identificar temas recurrentes (flora, fauna, agua,
     aire, etc.)
   - Paso 4: Sintetizar los temas más cuestionados, CITANDO documentos específicos
     como evidencia de cada tema

5. Buenas prácticas:
   - Para búsquedas semánticas: crea queries largos con sinónimos y conceptos
     relacionados
   - Para Cypher: usa LIMITs apropiados (5-10 docs para análisis de contenido
     completo)
   - Para extracción de contenido: SIEMPRE incluye metadatos junto con d.content:
     * d.id, d.filename, d.content
     * Proyecto: p.name
     * Ubicación: r.name (región), cm.name (comuna)
     * Tipo: pt.name (tipo proyecto), t.code (tipología)
     * Clasificaciones: collect(DISTINCT c.name) AS classes
   - Combina ambas herramientas cuando sea necesario
   - NO te limites a devolver resultados brutos: ANALIZA y SINTETIZA
   - Si el contenido es muy largo, enfócate en las partes más relevantes
   - SIEMPRE incluye las citas completas de documentos en tu respuesta final

6. Respuestas y Citación de Documentos:
   - Sé conciso pero completo
   - Explica tu proceso de análisis brevemente
   - SIEMPRE cita los documentos relevantes con todos sus detalles disponibles
   - SIEMPRE responde en español de Chile
   - Presenta hallazgos de forma estructurada (listas numeradas, categorías)

   IMPORTANTE - Formato de Citación de Documentos:
   Para CADA documento relevante que uses en tu respuesta, DEBES incluir:
   - ✅ Nombre del archivo (filename)
   - ✅ Proyecto al que pertenece
   - ✅ Región y comuna (si están disponibles)
   - ✅ Tipo de proyecto y tipología (si están disponibles)
   - ✅ Clases/clasificaciones del documento
   - ✅ ID del documento (doc_id) si es relevante para referencias futuras

   Ejemplo de citación correcta:
   "Según el documento 'Anexo 4 - Flora y Fauna.pdf' del proyecto 'Mina Los
   Andes' (Región de Antofagasta, Comuna Calama, tipología i1 - minería),
   clasificado como [Flora, Fauna, Línea Base], se identificó..."

   Nunca presentes resultados sin citar la fuente documental específica.
   Si extraes información de múltiples documentos, cita cada uno por separado.

7. Limitaciones y honestidad:
   - Si el contenido extraído es insuficiente para responder, dilo claramente
   - Si necesitas más documentos para un análisis robusto, menciónalo
   - Si no encuentras patrones claros, explica qué encontraste en su lugar

RECUERDA - Mentalidad Iterativa:
   🔄 NO te detengas después de usar una herramienta una sola vez
   🔄 Si el primer resultado es insuficiente, usa las herramientas nuevamente
   🔄 Combina herramientas: los resultados de Cypher pueden informar búsquedas
      semánticas y viceversa
   🔄 Itera hasta que tengas información suficiente para responder completamente
   🔄 Tu valor está en iterar inteligentemente sobre las herramientas Y en
      analizar el contenido devuelto para responder preguntas complejas que
      requieren síntesis e interpretación

   NO digas "no encontré información" si solo intentaste una vez.
   SIEMPRE intenta múltiples enfoques antes de concluir que no hay información.

IMPORTANTE - Cuándo DETENERTE y dar una respuesta final:
   🛑 DETENTE cuando tengas suficiente información para responder la pregunta
   🛑 Después de 5-7 llamadas a herramientas, evalúa si puedes dar una respuesta final.
   🛑 DETENTE cuando no hay progreso significativo, detente y genera una respuesta final con lo que tienes.
   """

    # Create tools list
    tools = [hybrid_search_tool, cypher_query_tool]

    # Create ReAct agent
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
    )

    return agent


def run_agent_query(
    query: str, verbose: bool = True, recursion_limit: int = 50
) -> dict:
    """Run a query through the ReAct agent.

    Parameters
    ----------
    query:
        User query in natural language (Spanish or English)
    verbose:
        Whether to print intermediate steps
    recursion_limit:
        Maximum number of iterations for the agent (default: 50).
        Increase for complex multi-step queries that require many tool calls.

    Returns
    -------
    dict
        Agent response containing messages and structured output if applicable
    """
    agent = create_react_agent()

    if verbose:
        print(f"\n{'=' * 80}")
        print(f"🤖 Query: {query}")
        print(f"{'=' * 80}\n")

    # Invoke agent with recursion limit configuration
    result = agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        config={"recursion_limit": recursion_limit},
    )

    if verbose:
        print(f"\n{'=' * 80}")
        print("📄 Agent Response:")
        print(f"{'=' * 80}")
        # Print the final AI message
        for msg in result["messages"]:
            if hasattr(msg, "type") and msg.type == "ai" and msg.content:
                print(msg.content)

    return result


if __name__ == "__main__":
    # Demonstration: Test the ReAct agent with different query types
    print("🚀 Testing ReAct Agent for Environmental Documents\n")

    # Test 1: Semantic search query
    print("\n" + "=" * 80)
    print("📌 TEST 1: Búsqueda semántica - Flora y Fauna")
    print("=" * 80)
    query1 = (
        "¿Qué documentos hablan sobre impactos en flora nativa y fauna "
        "vertebrada en proyectos mineros?"
    )
    result1 = run_agent_query(query1, verbose=True)

    # Test 2: Structured query (Cypher)
    print("\n" + "=" * 80)
    print("📌 TEST 2: Consulta estructurada - Estadísticas por región")
    print("=" * 80)
    query2 = "¿Cuántos documentos hay por región en la base de datos?"
    result2 = run_agent_query(query2, verbose=True)

    # Test 3: Combined query requiring iteration
    print("\n" + "=" * 80)
    print("📌 TEST 3: Consulta combinada - Filtrar y buscar contenido")
    print("=" * 80)
    query3 = (
        "Necesito documentos sobre energía renovable en la Región de "
        "Antofagasta que mencionen impacto en avifauna"
    )
    result3 = run_agent_query(query3, verbose=True)

    # Test 4: Complex multi-step analysis with content extraction
    print("\n" + "=" * 80)
    print("📌 TEST 4: Análisis complejo multi-paso - Preguntas frecuentes ICSARA")
    print("=" * 80)
    query4 = (
        "desde la comuna donde tienes más documentos ICSARA, "
        "dame las preguntas más frecuentes que hacen los evaluadores"
    )
    result4 = run_agent_query(query4, verbose=True)
    print("\n" + "=" * 50 + " Resultado ICSARA " + "=" * 50)
    print(result4["messages"][-1].content)
