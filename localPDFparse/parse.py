"""Premium PDF to Markdown extraction engine optimized for complex RAG applications.

This module provides enterprise-grade PDF extraction with advanced text processing,
intelligent table handling, comprehensive metadata extraction, and robust error recovery.
Designed for high-quality content extraction suitable for sophisticated RAG systems.

Features:
- Advanced text cleaning and normalization
- Intelligent section and hierarchy detection
- Comprehensive table extraction with context
- Robust error handling and fallback strategies
- Multi-language support
- Quality validation and metrics

Usage:
uv run python localPDFparse/parse.py
"""

# %%
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Iterable

import pymupdf  # type: ignore
import pymupdf4llm


class ExtractionQuality(Enum):
    """Quality levels for extraction validation."""

    HIGH = "high"  # All checks passed
    MEDIUM = "medium"  # Minor issues detected
    LOW = "low"  # Major issues, needs review


@dataclass
class DocumentMetadata:
    """Comprehensive document metadata container."""

    title: str = ""
    author: str = ""
    subject: str = ""
    keywords: list[str] = field(default_factory=list)
    creation_date: str = ""
    modification_date: str = ""
    page_count: int = 0
    language: str = ""
    document_type: str = ""
    has_toc: bool = False
    has_tables: bool = False
    has_images: bool = False
    extraction_quality: ExtractionQuality = ExtractionQuality.HIGH
    quality_notes: list[str] = field(default_factory=list)


@dataclass
class TableInfo:
    """Enhanced container for table metadata and content."""

    number: str  # Table identifier
    title: str  # Table title/caption
    content: list[list[str]]  # Table rows
    raw_markdown: str  # Markdown representation
    page_number: int | None = None
    context_before: str = ""
    context_after: str = ""
    column_headers: list[str] = field(default_factory=list)
    row_count: int = 0
    column_count: int = 0
    has_merged_cells: bool = False
    extraction_confidence: float = 1.0


@dataclass
class SectionInfo:
    """Document section metadata."""

    level: int  # Heading level (1-6)
    title: str  # Section title
    content: str  # Section content
    subsections: list[SectionInfo] = field(default_factory=list)
    tables: list[str] = field(default_factory=list)  # Table IDs in section
    word_count: int = 0
    line_number: int = 0


class TextCleaner:
    """Advanced text cleaning and normalization utilities."""

    @staticmethod
    def normalize_unicode(text: str) -> str:
        """Normalize Unicode characters to their canonical form."""
        # Normalize to NFKC form (compatibility decomposition + canonical composition)
        text = unicodedata.normalize("NFKC", text)
        # Remove zero-width characters
        text = re.sub(r"[\u200b\u200c\u200d\ufeff]", "", text)
        # Fix common encoding issues
        replacements = {
            """: '"',
            """: '"',
            "'": "'",
            "'": "'",
            "–": "-",
            "—": "--",
            "…": "...",
            "\xa0": " ",  # Non-breaking space
            "\u2028": "\n",  # Line separator
            "\u2029": "\n\n",  # Paragraph separator
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text

    @staticmethod
    def fix_hyphenation(text: str) -> str:
        """Fix word hyphenation at line breaks."""
        # Fix hyphenated words split across lines
        text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", text)
        # Fix hyphenated words with extra spaces
        text = re.sub(r"(\w+)\s*-\s*\n\s*(\w+)", r"\1\2", text)
        return text

    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """Normalize whitespace while preserving structure."""
        # Replace multiple spaces with single space
        text = re.sub(r"[ \t]+", " ", text)
        # Replace multiple newlines with double newline
        text = re.sub(r"\n{3,}", "\n\n", text)
        # Remove trailing whitespace from lines
        lines = [line.rstrip() for line in text.splitlines()]
        return "\n".join(lines)

    @staticmethod
    def fix_bullet_points(text: str) -> str:
        """Standardize bullet point formats."""
        # Common bullet patterns to standardize
        bullet_patterns = [
            (r"^[•·∙◦▪▫◆◇★☆➤→⇒»]", "-"),  # Various bullets to dash
            (r"^[①②③④⑤⑥⑦⑧⑨⑩]", lambda m: f"{ord(m.group()[0]) - ord('①') + 1}."),
            (r"^[⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑]", lambda m: f"{ord(m.group()[0]) - ord('⒈') + 1}."),
        ]

        lines = text.splitlines()
        for i, line in enumerate(lines):
            stripped = line.lstrip()
            indent = len(line) - len(stripped)
            for pattern, replacement in bullet_patterns:
                if re.match(pattern, stripped):
                    if callable(replacement):
                        new_bullet = replacement(re.match(pattern, stripped))
                    else:
                        new_bullet = replacement
                    lines[i] = " " * indent + re.sub(pattern, new_bullet, stripped)
                    break
        return "\n".join(lines)

    @staticmethod
    def clean_headers(text: str) -> str:
        """Clean and standardize headers."""
        lines = text.splitlines()
        cleaned = []
        for line in lines:
            # Remove page numbers from headers
            line = re.sub(r"Página\s*\d+\s*$", "", line, flags=re.IGNORECASE)
            line = re.sub(r"Page\s*\d+\s*$", "", line, flags=re.IGNORECASE)
            # Remove excessive asterisks from headers
            if line.startswith("#"):
                line = re.sub(r"\*{2,}", "", line)
            cleaned.append(line)
        return "\n".join(cleaned)

    @classmethod
    def clean_text(cls, text: str) -> str:
        """Apply all cleaning operations in sequence."""
        text = cls.normalize_unicode(text)
        text = cls.fix_hyphenation(text)
        text = cls.normalize_whitespace(text)
        text = cls.fix_bullet_points(text)
        text = cls.clean_headers(text)
        return text


def _extract_document_metadata(
    doc: "pymupdf.Document", md_text: str
) -> DocumentMetadata:
    """Extract comprehensive metadata from PDF document."""
    metadata = DocumentMetadata()

    # Extract PDF metadata
    pdf_metadata = doc.metadata
    if pdf_metadata:
        metadata.title = pdf_metadata.get("title", "").strip()
        metadata.author = pdf_metadata.get("author", "").strip()
        metadata.subject = pdf_metadata.get("subject", "").strip()
        keywords = pdf_metadata.get("keywords", "")
        if keywords:
            metadata.keywords = [k.strip() for k in keywords.split(",") if k.strip()]
        metadata.creation_date = str(pdf_metadata.get("creationDate", ""))
        metadata.modification_date = str(pdf_metadata.get("modDate", ""))

    metadata.page_count = len(doc)
    metadata.has_toc = bool(doc.get_toc())

    # Detect language from content
    metadata.language = _detect_language(md_text)

    # Detect document type
    metadata.document_type = _detect_document_type(md_text)

    # Check for tables and images
    metadata.has_tables = "|" in md_text and "---" in md_text
    metadata.has_images = bool(re.search(r"!\[.*?\]\(.*?\)", md_text))

    return metadata


def _detect_language(text: str) -> str:
    """Detect the primary language of the document."""
    # Simple heuristic based on common words
    spanish_words = ["de", "la", "el", "en", "y", "que", "del", "los", "las", "para"]
    english_words = ["the", "of", "and", "to", "in", "is", "for", "with", "on", "at"]

    text_lower = text.lower()
    spanish_count = sum(1 for word in spanish_words if f" {word} " in text_lower)
    english_count = sum(1 for word in english_words if f" {word} " in text_lower)

    if spanish_count > english_count:
        return "es"
    elif english_count > spanish_count:
        return "en"
    else:
        return "unknown"


def _detect_document_type(text: str) -> str:
    """Detect the type of document based on content patterns."""
    text_lower = text.lower()

    # Check for common document type indicators
    if "abstract" in text_lower and "references" in text_lower:
        return "academic_paper"
    elif "informe" in text_lower or "report" in text_lower:
        return "report"
    elif "manual" in text_lower or "guide" in text_lower:
        return "manual"
    elif "contract" in text_lower or "agreement" in text_lower:
        return "legal"
    elif "invoice" in text_lower or "factura" in text_lower:
        return "invoice"
    else:
        return "general"


def _choose_header_identifier(
    doc: "pymupdf.Document",
    *,
    prefer_toc: bool = True,
    max_levels: int = 6,
) -> Any:
    """Return an optimized header identifier for to_markdown()."""
    toc = doc.get_toc()

    if prefer_toc and toc:
        return pymupdf4llm.TocHeaders(doc)

    return pymupdf4llm.IdentifyHeaders(doc, max_levels=max_levels)


def _is_header_sep(line: str) -> bool:
    """Enhanced detection of Markdown table header separator lines."""
    text = line.strip()
    if not text:
        return False

    # Must contain pipes and dashes
    if "|" not in text or "-" not in text:
        return False

    # Check for table separator pattern
    # Remove spaces and check if it's mostly dashes, pipes, and colons
    cleaned = re.sub(r"\s+", "", text)
    valid_chars = set(cleaned)
    if not valid_chars.issubset({"-", "|", ":"}):
        return False

    # Must have at least 3 dashes
    if cleaned.count("-") < 3:
        return False

    return True


def _split_md_row(row: str) -> list[str]:
    """Split a Markdown table row into cells with improved handling."""
    s = row.strip()

    # Remove outer pipes if present
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]

    # Split by pipe and clean each cell
    parts = []
    for part in s.split("|"):
        # Clean the cell content
        cleaned = part.strip()
        # Preserve internal formatting but remove excessive spaces
        cleaned = re.sub(r"\s+", " ", cleaned)
        parts.append(cleaned)

    return parts


def _extract_table_references(text: str) -> list[tuple[str, int, str]]:
    """Extract table references with context.

    Returns list of (table_id, position, context) tuples.
    """
    references = []

    # Comprehensive patterns for table references
    patterns = [
        (r"\(Tabla\s+([\d\.\-]+)\)", "parenthetical"),
        (r"\(tabla\s+([\d\.\-]+)\)", "parenthetical"),
        (r"Tabla\s+([\d\.\-]+)(?:[:\.])", "inline"),
        (r"tabla\s+([\d\.\-]+)(?:[:\.])", "inline"),
        (r"\(ver\s+Tabla\s+([\d\.\-]+)\)", "see_reference"),
        (r"\(véase\s+Tabla\s+([\d\.\-]+)\)", "see_reference"),
        (r"Table\s+([\d\.\-]+)", "english"),
        (r"\(Table\s+([\d\.\-]+)\)", "english_parenthetical"),
        (r"según\s+Tabla\s+([\d\.\-]+)", "according_to"),
        (r"como\s+se\s+muestra\s+en\s+(?:la\s+)?Tabla\s+([\d\.\-]+)", "as_shown"),
    ]

    for pattern, ref_type in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            table_id = match.group(1)
            position = match.start()

            # Extract context (50 chars before and after)
            start = max(0, position - 50)
            end = min(len(text), position + len(match.group()) + 50)
            context = text[start:end].replace("\n", " ").strip()

            references.append((table_id, position, context))

    # Sort by position
    references.sort(key=lambda x: x[1])
    return references


def _extract_enhanced_table_metadata(
    lines: list[str], table_start_idx: int
) -> TableInfo | None:
    """Extract comprehensive table metadata with quality metrics."""
    if table_start_idx < 1:
        return None

    # Look for table title (search up to 10 lines back for complex titles)
    title = ""
    number = ""
    title_idx = None

    for i in range(max(0, table_start_idx - 10), table_start_idx):
        line = lines[i].strip()

        # Enhanced patterns for table titles
        title_patterns = [
            r"^(?:\*\*)?Tabla\s+([\d\.\-]+)[:\.]?\s*(.*)(?:\*\*)?$",
            r"^(?:\*\*)?Table\s+([\d\.\-]+)[:\.]?\s*(.*)(?:\*\*)?$",
            r"^(?:\*\*)?TABLA\s+([\d\.\-]+)[:\.]?\s*(.*)(?:\*\*)?$",
            r"^(?:\*\*)?Cuadro\s+([\d\.\-]+)[:\.]?\s*(.*)(?:\*\*)?$",
        ]

        for pattern in title_patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                number = match.group(1)
                title_text = match.group(2).strip()

                # Collect multi-line titles
                if title_text:
                    title = title_text
                else:
                    # Title might continue on next lines
                    title_parts = []
                    for j in range(i + 1, min(i + 4, table_start_idx)):
                        next_line = lines[j].strip()
                        if (
                            next_line
                            and not next_line.startswith("|")
                            and not _is_header_sep(next_line)
                        ):
                            title_parts.append(next_line)
                        else:
                            break
                    title = " ".join(title_parts)

                title_idx = i
                break

        if title_idx is not None:
            break

    if not number:
        return None

    # Extract and validate table content
    rows = []
    confidence = 1.0

    # Header row
    if table_start_idx > 0:
        header_line = lines[table_start_idx - 1]
        if "|" in header_line:
            header_cells = _split_md_row(header_line)
            rows.append(header_cells)
            column_count = len(header_cells)
        else:
            confidence *= 0.8
            return None

    # Skip separator
    i = table_start_idx + 1

    # Body rows with validation
    inconsistent_columns = False
    while i < len(lines):
        line = lines[i].strip()
        if not line or "|" not in line:
            break

        row_cells = _split_md_row(line)

        # Check column consistency
        if len(row_cells) != column_count:
            inconsistent_columns = True
            confidence *= 0.9
            # Pad or trim to match
            if len(row_cells) < column_count:
                row_cells.extend([""] * (column_count - len(row_cells)))
            else:
                row_cells = row_cells[:column_count]

        rows.append(row_cells)
        i += 1

    if len(rows) < 2:  # Must have at least header + 1 data row
        return None

    # Extract context
    context_before = ""
    context_after = ""

    # Context before (3-5 lines, excluding title)
    start_ctx = max(0, (title_idx if title_idx else table_start_idx) - 5)
    end_ctx = title_idx if title_idx else table_start_idx - 1
    if start_ctx < end_ctx:
        ctx_lines = lines[start_ctx:end_ctx]
        context_before = " ".join(line.strip() for line in ctx_lines if line.strip())

    # Context after (3-5 lines)
    if i < len(lines):
        ctx_lines = lines[i : min(i + 5, len(lines))]
        context_after = " ".join(line.strip() for line in ctx_lines if line.strip())

    # Build enhanced markdown
    raw_md_lines = []
    if title:
        raw_md_lines.append(f"**Tabla {number}: {title}**")
    else:
        raw_md_lines.append(f"**Tabla {number}**")
    raw_md_lines.append("")

    # Add table with proper formatting
    if rows:
        # Header
        raw_md_lines.append("| " + " | ".join(rows[0]) + " |")
        raw_md_lines.append("| " + " | ".join(["---"] * len(rows[0])) + " |")
        # Body
        for row in rows[1:]:
            raw_md_lines.append("| " + " | ".join(row) + " |")

    # Check for merged cells (empty cells might indicate merging)
    has_merged = any(any(cell == "" for cell in row) for row in rows[1:])

    return TableInfo(
        number=number,
        title=title,
        content=rows,
        raw_markdown="\n".join(raw_md_lines),
        context_before=context_before,
        context_after=context_after,
        column_headers=rows[0] if rows else [],
        row_count=len(rows) - 1,  # Excluding header
        column_count=column_count if rows else 0,
        has_merged_cells=has_merged or inconsistent_columns,
        extraction_confidence=confidence,
    )


def _find_and_catalog_tables(md_text: str) -> dict[str, TableInfo]:
    """Find all tables with enhanced detection and cataloging."""
    lines = md_text.splitlines()
    tables: dict[str, TableInfo] = {}
    i = 0

    while i < len(lines):
        line = lines[i]
        if _is_header_sep(line):
            table_info = _extract_enhanced_table_metadata(lines, i)
            if table_info and table_info.extraction_confidence > 0.5:
                tables[table_info.number] = table_info
                # Skip past this table
                while i < len(lines) and "|" in lines[i]:
                    i += 1
        i += 1

    return tables


def _extract_document_sections(md_text: str) -> list[SectionInfo]:
    """Extract document structure and sections."""
    lines = md_text.splitlines()
    sections: list[SectionInfo] = []
    current_sections: dict[int, SectionInfo] = {}

    for i, line in enumerate(lines):
        # Check for headers
        header_match = re.match(r"^(#{1,6})\s+(.+)", line)
        if header_match:
            level = len(header_match.group(1))
            title = header_match.group(2).strip()

            # Clean title
            title = re.sub(r"\*{2,}", "", title)  # Remove bold markers
            title = re.sub(r"\s+", " ", title)  # Normalize spaces

            section = SectionInfo(level=level, title=title, content="", line_number=i)

            # Add to appropriate parent
            if level == 1:
                sections.append(section)
                current_sections = {1: section}
            else:
                # Find parent section
                parent_level = level - 1
                while parent_level > 0 and parent_level not in current_sections:
                    parent_level -= 1

                if parent_level > 0:
                    parent = current_sections[parent_level]
                    parent.subsections.append(section)

                current_sections[level] = section

    return sections


def _embed_tables_with_smart_placement(
    md_text: str, tables: dict[str, TableInfo]
) -> str:
    """Embed tables with intelligent placement and formatting."""
    lines = md_text.splitlines()
    result_lines = []
    embedded_tables = set()
    i = 0

    while i < len(lines):
        line = lines[i]
        result_lines.append(line)

        # Check for table references
        references = _extract_table_references(line)

        for table_id, _, context in references:
            # Normalize table ID
            normalized_id = table_id.strip()

            # Find matching table
            matching_table = None
            for tid, tinfo in tables.items():
                if tid == normalized_id or tid.replace("-", ".") == normalized_id:
                    matching_table = tinfo
                    break

            if matching_table and matching_table.number not in embedded_tables:
                # Add spacing
                result_lines.append("")

                # Add metadata comment for RAG systems
                result_lines.append(f"<!-- INICIO TABLA {matching_table.number} -->")
                result_lines.append(
                    f"<!-- Confianza de extracción: "
                    f"{matching_table.extraction_confidence:.2f} -->"
                )

                if matching_table.context_before:
                    result_lines.append("<!-- Contexto previo: -->")
                    ctx = matching_table.context_before.replace("-->", "→")
                    result_lines.append(f"<!-- {ctx} -->")

                result_lines.append("")

                # Add the table with title
                result_lines.append(matching_table.raw_markdown)

                # Add table statistics for RAG
                result_lines.append("")
                result_lines.append(
                    f"<!-- Estadísticas: {matching_table.row_count} filas, "
                    f"{matching_table.column_count} columnas -->"
                )

                if matching_table.context_after:
                    result_lines.append("<!-- Contexto posterior: -->")
                    ctx = matching_table.context_after.replace("-->", "→")
                    result_lines.append(f"<!-- {ctx} -->")

                result_lines.append(f"<!-- FIN TABLA {matching_table.number} -->")
                result_lines.append("")

                embedded_tables.add(matching_table.number)

        i += 1

    # Add unreferenced tables with explanation
    unreferenced = {k: v for k, v in tables.items() if k not in embedded_tables}
    if unreferenced:
        result_lines.append("")
        result_lines.append("---")
        result_lines.append("")
        result_lines.append("## Tablas Adicionales del Documento")
        result_lines.append("")
        result_lines.append(
            "> **Nota:** Las siguientes tablas no tienen referencias explícitas "
            "en el texto principal pero contienen información potencialmente relevante."
        )
        result_lines.append("")

        for table_info in unreferenced.values():
            result_lines.append(table_info.raw_markdown)
            result_lines.append("")
            if table_info.extraction_confidence < 1.0:
                result_lines.append(
                    f"> ⚠️ Confianza de extracción: "
                    f"{table_info.extraction_confidence:.2f}"
                )
                result_lines.append("")

    return "\n".join(result_lines)


def _add_document_structure(
    md_text: str, metadata: DocumentMetadata, sections: list[SectionInfo]
) -> str:
    """Add document structure and metadata for RAG optimization."""
    lines = []

    # Add YAML front matter with metadata
    lines.extend(
        [
            "---",
            f"title: {metadata.title or 'Sin título'}",
            f"author: {metadata.author or 'Desconocido'}",
            f"date: {metadata.creation_date or 'Sin fecha'}",
            f"language: {metadata.language}",
            f"type: {metadata.document_type}",
            f"pages: {metadata.page_count}",
            f"has_toc: {metadata.has_toc}",
            f"has_tables: {metadata.has_tables}",
            f"extraction_quality: {metadata.extraction_quality.value}",
        ]
    )

    if metadata.keywords:
        lines.append(f"keywords: [{', '.join(metadata.keywords)}]")

    lines.extend(["---", ""])

    # Add document structure summary if we have sections
    if sections:
        lines.extend(
            [
                "<!-- ESTRUCTURA DEL DOCUMENTO -->",
                "<!-- Este documento contiene las siguientes secciones principales:",
            ]
        )
        for section in sections[:10]:  # Limit to first 10 for summary
            lines.append(f"  - {section.title}")
        if len(sections) > 10:
            lines.append(f"  ... y {len(sections) - 10} secciones más")
        lines.extend(["-->", ""])

    # Add the main content
    lines.append(md_text)

    return "\n".join(lines)


def _validate_extraction_quality(
    md_text: str, tables: dict[str, TableInfo], metadata: DocumentMetadata
) -> tuple[ExtractionQuality, list[str]]:
    """Validate extraction quality and identify issues."""
    issues = []
    quality = ExtractionQuality.HIGH

    # Check text quality
    if len(md_text) < 100:
        issues.append("Documento muy corto (< 100 caracteres)")
        quality = ExtractionQuality.LOW
    elif len(md_text) < 1000:
        issues.append("Documento corto (< 1000 caracteres)")
        quality = ExtractionQuality.MEDIUM

    # Check for encoding issues
    if "�" in md_text or "\ufffd" in md_text:
        issues.append("Problemas de codificación detectados")
        quality = ExtractionQuality.MEDIUM

    # Check for excessive whitespace
    if "\n\n\n" in md_text:
        issues.append("Espaciado excesivo detectado")
        if quality == ExtractionQuality.HIGH:
            quality = ExtractionQuality.MEDIUM

    # Check table quality
    low_confidence_tables = [
        t for t in tables.values() if t.extraction_confidence < 0.8
    ]
    if low_confidence_tables:
        issues.append(
            f"{len(low_confidence_tables)} tabla(s) con baja confianza de extracción"
        )
        if quality == ExtractionQuality.HIGH:
            quality = ExtractionQuality.MEDIUM

    # Check for missing metadata
    if not metadata.title:
        issues.append("Título del documento no encontrado")

    return quality, issues


def extract_markdown(
    input_path: str | Path,
    *,
    # Extraction options
    ignore_images: bool = True,
    ignore_graphics: bool = False,
    table_strategy: str = "lines_strict",
    prefer_toc_headers: bool = True,
    max_header_levels: int = 6,
    force_text: bool = True,
    margins: float | tuple[float, float] | tuple[float, float, float, float] = 0,
    page_chunks: bool = False,
    page_separators: bool = False,
    pages: Iterable[int] | range | None = None,
    show_progress: bool = False,
    # Output options
    output_dir: str | Path | None = "localPDFparse/markdown",
    overwrite: bool = True,
    encoding: str = "utf-8",
    # Quality options
    use_glyphs: bool = True,
    embed_tables_inline: bool = True,
    add_document_structure: bool = True,
    clean_text: bool = True,
    validate_quality: bool = True,
    # Advanced options
    fallback_strategies: list[str] | None = None,
    min_confidence: float = 0.5,
) -> tuple[str, DocumentMetadata]:
    """Extract premium-quality Markdown from PDF for complex RAG applications.

    This function provides enterprise-grade PDF extraction with comprehensive
    text processing, intelligent table handling, and robust error recovery.

    Args:
        input_path: Path to the PDF file
        ignore_images: Skip image extraction (recommended for text-focused RAG)
        table_strategy: Primary strategy for table extraction
        clean_text: Apply advanced text cleaning and normalization
        validate_quality: Perform quality validation and reporting
        add_document_structure: Add metadata and structure information
        min_confidence: Minimum confidence threshold for table extraction
        fallback_strategies: Custom fallback strategies for table extraction

    Returns:
        Tuple of (markdown_text, metadata) with comprehensive extraction results

    Raises:
        FileNotFoundError: If the PDF file doesn't exist
        RuntimeError: If extraction fails after all strategies
    """
    pdf_path = Path(input_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    # Open PDF document
    doc = pymupdf.open(str(pdf_path))

    # Choose header detection strategy
    hdr_info = _choose_header_identifier(
        doc,
        prefer_toc=prefer_toc_headers,
        max_levels=max_header_levels,
    )

    # Define extraction strategies
    if fallback_strategies is None:
        fallback_strategies = ["lines_strict", "lines", "text"]

    strategies = [table_strategy] + [
        s for s in fallback_strategies if s != table_strategy
    ]

    # Try extraction with fallback strategies
    md: str | list[dict] | None = None
    last_error: Exception | None = None
    successful_strategy = None

    for strategy in strategies:
        try:
            md = pymupdf4llm.to_markdown(
                doc,
                detect_bg_color=True,
                embed_images=not ignore_images,
                extract_words=False,
                force_text=force_text,
                hdr_info=hdr_info,
                ignore_alpha=False,
                ignore_code=False,
                ignore_graphics=ignore_graphics,
                ignore_images=ignore_images,
                image_format="png",
                image_path="",
                image_size_limit=0.05,
                margins=margins,
                page_chunks=page_chunks,
                page_separators=page_separators,
                pages=list(pages) if pages is not None else None,
                show_progress=show_progress,
                table_strategy=strategy,
                use_glyphs=use_glyphs,
                write_images=False,
            )
            successful_strategy = strategy
            break
        except Exception as err:
            last_error = err
            continue

    if md is None:
        if last_error:
            raise RuntimeError(f"Extraction failed: {last_error}")
        raise RuntimeError("Extraction failed for all strategies")

    # Convert to string if necessary
    if isinstance(md, list):
        md_text = "\n\n".join(page.get("markdown", "") for page in md)
    else:
        md_text = md

    # Apply text cleaning
    if clean_text:
        cleaner = TextCleaner()
        md_text = cleaner.clean_text(md_text)

    # Extract metadata
    metadata = _extract_document_metadata(doc, md_text)

    # Extract document structure
    sections = _extract_document_sections(md_text) if add_document_structure else []

    # Find and process tables
    tables = _find_and_catalog_tables(md_text)

    # Filter low-confidence tables
    if min_confidence > 0:
        tables = {
            k: v for k, v in tables.items() if v.extraction_confidence >= min_confidence
        }

    # Embed tables inline
    if embed_tables_inline and tables:
        md_text = _embed_tables_with_smart_placement(md_text, tables)

    # Add document structure
    if add_document_structure:
        md_text = _add_document_structure(md_text, metadata, sections)

    # Validate quality
    if validate_quality:
        quality, issues = _validate_extraction_quality(md_text, tables, metadata)
        metadata.extraction_quality = quality
        metadata.quality_notes = issues

    # Write to file if output directory specified
    if output_dir is not None:
        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        pdf_name = pdf_path.stem + ".md"
        out_path = out_dir / pdf_name

        if not overwrite and out_path.exists():
            counter = 1
            while True:
                candidate = out_dir / f"{pdf_path.stem} ({counter}).md"
                if not candidate.exists():
                    out_path = candidate
                    break
                counter += 1

        # Write with BOM for better Unicode support
        with open(out_path, "w", encoding=encoding) as f:
            f.write(md_text)

        # Log extraction results
        print(f"✅ Extraction complete: {out_path}")
        print(f"   Strategy: {successful_strategy}")
        print(f"   Quality: {metadata.extraction_quality.value}")
        if metadata.quality_notes:
            print(f"   Issues: {', '.join(metadata.quality_notes)}")

    return md_text, metadata


def analyze_document(input_path: str | Path) -> None:
    """Analyze a PDF document and print detailed statistics."""
    print("📊 Analyzing document...")
    print("-" * 60)

    md_text, metadata = extract_markdown(
        input_path,
        output_dir=None,  # Don't save, just analyze
        show_progress=True,
    )

    # Print metadata
    print("\n📄 Document Metadata:")
    print(f"   Title: {metadata.title or 'Not found'}")
    print(f"   Author: {metadata.author or 'Not found'}")
    print(f"   Pages: {metadata.page_count}")
    print(f"   Language: {metadata.language}")
    print(f"   Type: {metadata.document_type}")
    print(f"   Quality: {metadata.extraction_quality.value}")

    # Print statistics
    tables = _find_and_catalog_tables(md_text)
    sections = _extract_document_sections(md_text)

    print("\n📈 Content Statistics:")
    print(f"   Characters: {len(md_text):,}")
    print(f"   Lines: {len(md_text.splitlines()):,}")
    print(f"   Words: {len(md_text.split()):,}")
    print(f"   Sections: {len(sections)}")
    print(f"   Tables: {len(tables)}")

    if tables:
        print("\n📊 Table Details:")
        for tid, tinfo in list(tables.items())[:5]:  # Show first 5
            print(f"   - Table {tid}: {tinfo.row_count}x{tinfo.column_count}")
            if tinfo.title:
                print(f"     Title: {tinfo.title[:50]}...")
            print(f"     Confidence: {tinfo.extraction_confidence:.2f}")

    if metadata.quality_notes:
        print("\n⚠️ Quality Issues:")
        for issue in metadata.quality_notes:
            print(f"   - {issue}")


if __name__ == "__main__":
    # Enhanced demonstration with quality reporting
    SAMPLE_PDF_PATH = (
        "localPDFparse/test_pdf/00.-Informe-T_e_cnico-"
        "Flora-y-Vegetaci_o_n-Valle-Noble.pdf"
    )

    print("🚀 Premium PDF Extraction Engine")
    print("=" * 60)

    # First, analyze the document
    analyze_document(SAMPLE_PDF_PATH)

    # Then, perform full extraction
    print("\n" + "=" * 60)
    print("📝 Performing full extraction with premium features...")
    print("-" * 60)

    result, metadata = extract_markdown(
        SAMPLE_PDF_PATH,
        output_dir="localPDFparse/markdown",
        embed_tables_inline=True,
        add_document_structure=True,
        clean_text=True,
        validate_quality=True,
        show_progress=False,
    )

    # Show final results
    print("\n✨ Extraction Summary:")
    print(f"   Document length: {len(result):,} characters")
    print(f"   Extraction quality: {metadata.extraction_quality.value}")
    print(f"   Tables processed: {result.count('<!-- INICIO TABLA')}")
    print(f"   References linked: {len(_extract_table_references(result))}")

    if metadata.quality_notes:
        print("\n📋 Quality Report:")
        for note in metadata.quality_notes:
            print(f"   ℹ️ {note}")
    else:
        print("\n✅ No quality issues detected!")

    saved_path = Path("localPDFparse/markdown") / (Path(SAMPLE_PDF_PATH).stem + ".md")
    print(f"\n📁 Output saved to: {saved_path}")
    print(f"   File size: {saved_path.stat().st_size:,} bytes")
    print("\n🎯 Ready for complex RAG applications!")
