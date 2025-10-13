"""Helper script to load JSON documents back into LangChain Document objects.

This script demonstrates how to load the saved JSON documents back into
LangChain Document objects for vector store upload or other processing.

Usage:
    uv run python PrepareDocsForUpsert/OneToOneDocs/load_documents.py
"""

# %%
from __future__ import annotations

import json
from pathlib import Path

from langchain_core.documents import Document


def load_document_from_json(json_path: Path) -> Document:
    """Load a LangChain Document from JSON file.

    Args:
        json_path: Path to JSON file containing document data

    Returns:
        LangChain Document object
    """
    with json_path.open("r", encoding="utf-8") as f:
        doc_dict = json.load(f)

    return Document(
        page_content=doc_dict["page_content"], metadata=doc_dict["metadata"]
    )


def load_all_documents(documents_dir: Path) -> list[Document]:
    """Load all documents from a directory.

    Args:
        documents_dir: Directory containing JSON document files

    Returns:
        List of LangChain Document objects
    """
    json_files = sorted(documents_dir.glob("*.json"))
    documents = []

    print(f"Loading {len(json_files)} documents from {documents_dir}...")

    for i, json_file in enumerate(json_files, 1):
        doc = load_document_from_json(json_file)
        documents.append(doc)

        if i % 1000 == 0:
            print(f"Loaded {i}/{len(json_files)} documents...")

    print(f"Successfully loaded {len(documents)} documents")
    return documents


def filter_documents_by_class(
    documents: list[Document], class_name: str
) -> list[Document]:
    """Filter documents by a specific class.

    Args:
        documents: List of Document objects
        class_name: Name of the class to filter by

    Returns:
        List of filtered Document objects
    """
    filtered = []
    for doc in documents:
        classes = doc.metadata.get("classes", [])
        for cls in classes:
            if isinstance(cls, dict) and cls.get("class") == class_name:
                filtered.append(doc)
                break
    return filtered


def main() -> None:
    """Demonstrate loading and filtering documents."""
    # Define paths
    base_dir = Path(__file__).parent.parent.parent
    documents_dir = (
        base_dir / "PrepareDocsForUpsert" / "OneToOneDocs" / ("documents_to_upsert")
    )

    print("=" * 80)
    print("Document Loader Demonstration")
    print("=" * 80)
    print()

    # Load a single document as example
    json_files = list(documents_dir.glob("*.json"))
    if not json_files:
        print("ERROR: No documents found!")
        return

    sample_doc = load_document_from_json(json_files[0])
    print(f"Sample document: {json_files[0].name}")
    print(f"Page content length: {len(sample_doc.page_content)} chars")
    # Access metadata as a dict
    doc_metadata = dict(sample_doc.metadata)
    metadata_keys = list(doc_metadata.keys())
    print(f"Metadata keys: {metadata_keys}")
    print(f"Classes: {[c['class'] for c in doc_metadata['classes']]}")
    print(f"Project: {doc_metadata['seaProjectName']}")
    print(f"Region: {doc_metadata['seaProjectRegion']}")
    print()

    # Load first 100 documents as example
    print("=" * 80)
    print("Loading sample documents...")
    print("=" * 80)
    documents = []
    for json_file in json_files[:100]:
        doc = load_document_from_json(json_file)
        documents.append(doc)

    print(f"Loaded {len(documents)} sample documents")
    print()

    # Filter by class
    flora_docs = filter_documents_by_class(documents, "Flora")
    fauna_docs = filter_documents_by_class(documents, "Fauna")
    linea_base_docs = filter_documents_by_class(documents, "Línea Base")

    print("=" * 80)
    print("Document Statistics (first 100)")
    print("=" * 80)
    print(f"Total documents: {len(documents)}")
    print(f"Flora documents: {len(flora_docs)}")
    print(f"Fauna documents: {len(fauna_docs)}")
    print(f"Línea Base documents: {len(linea_base_docs)}")
    print()

    print("=" * 80)
    print("Ready for Vector Store Upload")
    print("=" * 80)
    print("These documents can now be uploaded to your vector store of choice:")
    print("- Pinecone")
    print("- Weaviate")
    print("- ChromaDB")
    print("- FAISS")
    print("- Qdrant")
    print("- Any other LangChain-compatible vector store")
    print()
    print(
        "Example for ChromaDB:\n"
        "  from langchain_community.vectorstores import Chroma\n"
        "  from langchain_openai import OpenAIEmbeddings\n"
        "\n"
        "  embeddings = OpenAIEmbeddings()\n"
        "  vectorstore = Chroma.from_documents(\n"
        "      documents=documents,\n"
        "      embedding=embeddings,\n"
        "      persist_directory='./chroma_db'\n"
        "  )\n"
    )


if __name__ == "__main__":
    main()
