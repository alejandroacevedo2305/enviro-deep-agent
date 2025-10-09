"""Comprehensive analysis of PDF parsing failures.

This script analyzes failed parsing logs to identify root causes, patterns,
and potential solutions for PDF extraction failures.
"""

# %%
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pandas as pd
import yaml


@dataclass
class FailurePattern:
    """Represents a failure pattern with metadata."""

    error_type: str
    error_message: str
    count: int = 0
    file_identifiers: list[str] = field(default_factory=list)
    s3_keys: list[str] = field(default_factory=list)
    from_compressed: int = 0
    file_sizes: list[float] = field(default_factory=list)
    document_types: Counter = field(default_factory=Counter)
    regions: Counter = field(default_factory=Counter)


@dataclass
class FailureAnalysis:
    """Comprehensive analysis of all failures."""

    total_failures: int
    patterns: dict[str, FailurePattern]
    error_categories: dict[str, list[FailurePattern]]
    recommendations: list[str]
    statistics: dict[str, Any]


def parse_failed_markdown(file_path: Path) -> dict[str, Any]:
    """Parse a failed markdown file and extract metadata and error info.

    Args:
        file_path: Path to the FAILED-*.md file

    Returns:
        Dictionary with parsed information
    """
    content = file_path.read_text(encoding="utf-8", errors="ignore")

    # Try to parse YAML frontmatter
    metadata = {}
    if content.startswith("---"):
        try:
            yaml_end = content.find("---", 3)
            if yaml_end > 0:
                yaml_content = content[3:yaml_end].strip()
                metadata = yaml.safe_load(yaml_content)
        except Exception as e:
            print(f"Warning: Failed to parse YAML in {file_path.name}: {e}")

    # Extract error information from content
    error_message = metadata.get("error", "Unknown error")
    error_type = metadata.get("error_type", "Exception")

    # Look for specific error patterns in the content
    if "Extraction failed:" in content:
        match = re.search(r"Extraction failed: (.+)", content)
        if match:
            error_message = match.group(1).strip()

    if "weakly-referenced object no longer exists" in error_message:
        error_type = "WeakReferenceError"
    elif "not a textpage of this page" in error_message:
        error_type = "TextPageError"
    elif "child process terminated abruptly" in error_message:
        error_type = "ProcessPoolError"
    elif "File is not a zip file" in error_message:
        error_type = "ZipFileError"
    elif "Timeout" in error_message or "timeout" in error_message:
        error_type = "TimeoutError"

    return {
        "file_identifier": metadata.get("file_identifier", ""),
        "s3_key": metadata.get("s3_key", ""),
        "error_type": error_type,
        "error_message": error_message,
        "from_compressed": metadata.get("from_compressed_file", False),
        "region": metadata.get("region", "Unknown"),
        "tipo_proyecto": metadata.get("tipo_proyecto", "Unknown"),
        "nombre": metadata.get("nombre", ""),
        "fecha_presentacion": metadata.get("fecha_presentacion", ""),
        "raw_content": content,
    }


def categorize_errors(
    failures: list[dict[str, Any]]
) -> dict[str, list[dict[str, Any]]]:
    """Categorize failures by error type.

    Args:
        failures: List of parsed failure dictionaries

    Returns:
        Dictionary mapping error categories to failure lists
    """
    categories = defaultdict(list)

    for failure in failures:
        error_type = failure["error_type"]
        error_msg = failure["error_message"].lower()

        # Main categories
        if "weakly-referenced" in error_msg or "weakreference" in error_type.lower():
            category = "Weak Reference Errors"
        elif "textpage" in error_msg or "textpage" in error_type.lower():
            category = "TextPage Errors"
        elif "process" in error_msg and "terminated" in error_msg:
            category = "Process Pool Errors"
        elif "zip" in error_msg:
            category = "ZIP File Errors"
        elif "timeout" in error_msg:
            category = "Timeout Errors"
        elif "memory" in error_msg:
            category = "Memory Errors"
        elif "extraction failed" in error_msg:
            category = "PyMuPDF Extraction Errors"
        else:
            category = "Other Errors"

        categories[category].append(failure)

    return dict(categories)


def analyze_patterns(failures: list[dict[str, Any]]) -> dict[str, FailurePattern]:
    """Analyze failure patterns and create pattern objects.

    Args:
        failures: List of parsed failure dictionaries

    Returns:
        Dictionary mapping pattern keys to FailurePattern objects
    """
    patterns = {}

    for failure in failures:
        error_type = failure["error_type"]
        error_message = failure["error_message"]

        # Create a pattern key
        pattern_key = f"{error_type}::{error_message[:100]}"

        if pattern_key not in patterns:
            patterns[pattern_key] = FailurePattern(
                error_type=error_type,
                error_message=error_message,
            )

        pattern = patterns[pattern_key]
        pattern.count += 1
        pattern.file_identifiers.append(failure["file_identifier"])
        pattern.s3_keys.append(failure["s3_key"])

        if failure["from_compressed"]:
            pattern.from_compressed += 1

        pattern.regions[failure["region"]] += 1
        pattern.document_types[failure["tipo_proyecto"]] += 1

    return patterns


def generate_recommendations(
    categories: dict[str, list[dict[str, Any]]]
) -> list[str]:
    """Generate actionable recommendations based on failure analysis.

    Args:
        categories: Categorized failures

    Returns:
        List of recommendation strings
    """
    recommendations = []

    # Analyze each category
    for category, failures in categories.items():
        count = len(failures)
        percentage = (count / sum(len(f) for f in categories.values())) * 100

        if category == "Weak Reference Errors":
            recommendations.append(
                f"🔧 **{category}** ({count} failures, {percentage:.1f}%):\n"
                "   - Cause: PyMuPDF objects being garbage collected during extraction\n"
                "   - Solution: Implement proper object lifecycle management\n"
                "   - Action: Keep document references alive during extraction\n"
                "   - Fix: Use context managers or explicit close() calls"
            )

        elif category == "TextPage Errors":
            recommendations.append(
                f"🔧 **{category}** ({count} failures, {percentage:.1f}%):\n"
                "   - Cause: Trying to access text from non-text pages (images/scans)\n"
                "   - Solution: Check page type before text extraction\n"
                "   - Action: Implement OCR fallback for image-based pages\n"
                "   - Fix: Use page.get_text() with error handling"
            )

        elif category == "Process Pool Errors":
            recommendations.append(
                f"🔧 **{category}** ({count} failures, {percentage:.1f}%):\n"
                "   - Cause: Child process crashes due to memory or corruption\n"
                "   - Solution: Implement per-file process isolation\n"
                "   - Action: Add memory limits and timeout per PDF\n"
                "   - Fix: Use multiprocessing with proper error boundaries"
            )

        elif category == "ZIP File Errors":
            recommendations.append(
                f"🔧 **{category}** ({count} failures, {percentage:.1f}%):\n"
                "   - Cause: Metadata incorrectly identifies PDFs as ZIP files\n"
                "   - Solution: Validate file type before processing\n"
                "   - Action: Check magic bytes, not file extension\n"
                "   - Fix: Add file type detection layer"
            )

        elif category == "PyMuPDF Extraction Errors":
            recommendations.append(
                f"🔧 **{category}** ({count} failures, {percentage:.1f}%):\n"
                "   - Cause: Various PyMuPDF internal errors\n"
                "   - Solution: Implement fallback extraction methods\n"
                "   - Action: Try multiple extraction strategies\n"
                "   - Fix: Use pdfplumber or pypdf as fallbacks"
            )

    # General recommendations
    recommendations.append(
        "\n📋 **General Recommendations**:\n"
        "   1. Implement retry logic with exponential backoff\n"
        "   2. Add file validation before processing (magic bytes, size, corruption)\n"
        "   3. Use timeouts for each PDF (suggest 5 minutes per file)\n"
        "   4. Add memory monitoring and limits per process\n"
        "   5. Implement OCR fallback for image-based PDFs\n"
        "   6. Keep PyMuPDF document objects in scope during extraction\n"
        "   7. Add detailed logging for debugging specific failures\n"
        "   8. Consider alternative parsers (pdfplumber, pypdf) as fallbacks"
    )

    return recommendations


def create_detailed_report(
    analysis: FailureAnalysis, output_path: Path
) -> None:
    """Create a detailed markdown report of the failure analysis.

    Args:
        analysis: FailureAnalysis object with all data
        output_path: Path to save the report
    """
    lines = [
        "# PDF Parsing Failures - Detailed Analysis",
        "",
        f"**Total Failures Analyzed:** {analysis.total_failures}",
        "",
        "## Executive Summary",
        "",
    ]

    # Add statistics
    lines.extend(
        [
            "### Key Statistics",
            "",
            f"- **Total Unique Error Patterns:** {len(analysis.patterns)}",
            f"- **Error Categories:** {len(analysis.error_categories)}",
            (
                f"- **Failures from Compressed Files:** "
                f"{analysis.statistics.get('from_compressed', 0)} "
                f"({analysis.statistics.get('from_compressed_pct', 0):.1f}%)"
            ),
            "",
        ]
    )

    # Add error categories breakdown
    lines.extend(["## Error Categories Breakdown", ""])

    for category, failures in sorted(
        analysis.error_categories.items(),
        key=lambda x: len(x[1]),
        reverse=True,
    ):
        count = len(failures)
        percentage = (count / analysis.total_failures) * 100
        lines.extend(
            [
                f"### {category}",
                "",
                f"**Count:** {count} ({percentage:.1f}% of total)",
                "",
            ]
        )

        # Show sample failures
        lines.append("**Sample Errors:**")
        lines.append("")
        for failure in failures[:3]:  # Show first 3
            lines.append(f"- `{failure['file_identifier']}`")
            lines.append(f"  - Error: {failure['error_message'][:100]}...")
            lines.append(f"  - Region: {failure['region']}")
            lines.append(f"  - Project: {failure['tipo_proyecto'][:50]}")
        lines.append("")

    # Add recommendations
    lines.extend(["## Recommendations", ""])
    for rec in analysis.recommendations:
        lines.append(rec)
        lines.append("")

    # Add detailed pattern analysis
    lines.extend(["## Detailed Pattern Analysis", ""])

    for pattern_key, pattern in sorted(
        analysis.patterns.items(),
        key=lambda x: x[1].count,
        reverse=True,
    )[:20]:  # Top 20 patterns
        lines.extend(
            [
                f"### Pattern: {pattern.error_type}",
                "",
                f"**Occurrences:** {pattern.count}",
                "",
                f"**Error Message:** `{pattern.error_message[:200]}`",
                "",
                f"**From Compressed Files:** {pattern.from_compressed} "
                f"({pattern.from_compressed/pattern.count*100:.1f}%)",
                "",
            ]
        )

        if pattern.regions:
            lines.append("**Regions Affected:**")
            for region, cnt in pattern.regions.most_common(5):
                lines.append(f"- {region}: {cnt}")
            lines.append("")

        if pattern.document_types:
            lines.append("**Document Types:**")
            for doc_type, cnt in pattern.document_types.most_common(3):
                lines.append(f"- {doc_type[:50]}: {cnt}")
            lines.append("")

    # Write the report
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ Detailed report saved to: {output_path}")


def analyze_failures(
    failures_dir: Path,
) -> FailureAnalysis:
    """Main analysis function.

    Args:
        failures_dir: Directory containing FAILED-*.md files

    Returns:
        FailureAnalysis object with complete analysis
    """
    print("🔍 Analyzing PDF parsing failures...")
    print(f"📁 Source directory: {failures_dir}")
    print()

    # Find all failed files
    failed_files = list(failures_dir.glob("FAILED-*.md"))
    print(f"📊 Found {len(failed_files)} failed files")

    if not failed_files:
        print("❌ No failed files found!")
        return FailureAnalysis(
            total_failures=0,
            patterns={},
            error_categories={},
            recommendations=[],
            statistics={},
        )

    # Parse all failures
    print("🔬 Parsing failure logs...")
    failures = []
    for file_path in failed_files:
        try:
            failure_data = parse_failed_markdown(file_path)
            failures.append(failure_data)
        except Exception as e:
            print(f"⚠️  Warning: Failed to parse {file_path.name}: {e}")

    print(f"✅ Successfully parsed {len(failures)} failure logs")
    print()

    # Categorize errors
    print("📂 Categorizing errors...")
    categories = categorize_errors(failures)

    for category, items in sorted(
        categories.items(), key=lambda x: len(x[1]), reverse=True
    ):
        print(f"   - {category}: {len(items)}")
    print()

    # Analyze patterns
    print("🔎 Analyzing failure patterns...")
    patterns = analyze_patterns(failures)
    print(f"   Found {len(patterns)} unique error patterns")
    print()

    # Calculate statistics
    from_compressed = sum(1 for f in failures if f["from_compressed"])
    statistics = {
        "from_compressed": from_compressed,
        "from_compressed_pct": (from_compressed / len(failures) * 100)
        if failures
        else 0,
        "total_files": len(failures),
    }

    # Generate recommendations
    print("💡 Generating recommendations...")
    recommendations = generate_recommendations(categories)
    print(f"   Generated {len(recommendations)} recommendations")
    print()

    return FailureAnalysis(
        total_failures=len(failures),
        patterns=patterns,
        error_categories=categories,
        recommendations=recommendations,
        statistics=statistics,
    )


def create_summary_table(analysis: FailureAnalysis) -> pd.DataFrame:
    """Create a summary table of error categories.

    Args:
        analysis: FailureAnalysis object

    Returns:
        DataFrame with summary statistics
    """
    rows = []

    for category, failures in analysis.error_categories.items():
        count = len(failures)
        percentage = (count / analysis.total_failures * 100) if analysis.total_failures else 0
        from_compressed = sum(1 for f in failures if f["from_compressed"])

        rows.append(
            {
                "Category": category,
                "Count": count,
                "Percentage": f"{percentage:.1f}%",
                "From Compressed": from_compressed,
                "Compressed %": (
                    f"{from_compressed/count*100:.1f}%" if count > 0 else "0%"
                ),
            }
        )

    df = pd.DataFrame(rows)
    df = df.sort_values("Count", ascending=False)
    return df


def export_analysis_data(
    analysis: FailureAnalysis, output_dir: Path
) -> None:
    """Export analysis data to various formats for further investigation.

    Args:
        analysis: FailureAnalysis object
        output_dir: Directory to save exports
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # Export summary table
    summary_df = create_summary_table(analysis)
    summary_path = output_dir / "failure_summary.csv"
    summary_df.to_csv(summary_path, index=False)
    print(f"📊 Summary table saved to: {summary_path}")

    # Export detailed patterns
    patterns_data = []
    for pattern_key, pattern in analysis.patterns.items():
        patterns_data.append(
            {
                "error_type": pattern.error_type,
                "error_message": pattern.error_message[:200],
                "count": pattern.count,
                "from_compressed_count": pattern.from_compressed,
                "sample_file_ids": ", ".join(pattern.file_identifiers[:5]),
                "top_regions": ", ".join(
                    [f"{k}({v})" for k, v in pattern.regions.most_common(3)]
                ),
            }
        )

    patterns_df = pd.DataFrame(patterns_data)
    patterns_df = patterns_df.sort_values("count", ascending=False)
    patterns_path = output_dir / "failure_patterns.csv"
    patterns_df.to_csv(patterns_path, index=False)
    print(f"📊 Patterns data saved to: {patterns_path}")

    # Export categories breakdown
    categories_data = []
    for category, failures in analysis.error_categories.items():
        for failure in failures:
            categories_data.append(
                {
                    "category": category,
                    "file_identifier": failure["file_identifier"],
                    "error_type": failure["error_type"],
                    "error_message": failure["error_message"][:200],
                    "from_compressed": failure["from_compressed"],
                    "region": failure["region"],
                    "tipo_proyecto": failure["tipo_proyecto"][:100],
                    "s3_key": failure["s3_key"],
                }
            )

    categories_df = pd.DataFrame(categories_data)
    categories_path = output_dir / "failure_details.csv"
    categories_df.to_csv(categories_path, index=False)
    print(f"📊 Detailed failures saved to: {categories_path}")

    # Export JSON for programmatic access
    json_data = {
        "total_failures": analysis.total_failures,
        "statistics": analysis.statistics,
        "categories": {
            cat: len(failures)
            for cat, failures in analysis.error_categories.items()
        },
        "top_patterns": [
            {
                "error_type": p.error_type,
                "error_message": p.error_message[:200],
                "count": p.count,
            }
            for p in sorted(
                analysis.patterns.values(), key=lambda x: x.count, reverse=True
            )[:20]
        ],
    }

    json_path = output_dir / "failure_analysis.json"
    json_path.write_text(json.dumps(json_data, indent=2), encoding="utf-8")
    print(f"📊 JSON analysis saved to: {json_path}")


if __name__ == "__main__":
    # Configuration
    FAILURES_DIR = Path("SimpleWorkflow/ParsingFailsSamples")
    OUTPUT_DIR = Path("SimpleWorkflow/failure_analysis")

    print("=" * 70)
    print("PDF PARSING FAILURES - COMPREHENSIVE ANALYSIS")
    print("=" * 70)
    print()

    # Run analysis
    analysis = analyze_failures(FAILURES_DIR)

    if analysis.total_failures == 0:
        print("❌ No failures to analyze!")
        exit(1)

    # Display summary
    print("=" * 70)
    print("ANALYSIS RESULTS")
    print("=" * 70)
    print()

    summary_df = create_summary_table(analysis)
    print(summary_df.to_string(index=False))
    print()

    # Display recommendations
    print("=" * 70)
    print("RECOMMENDATIONS")
    print("=" * 70)
    print()
    for rec in analysis.recommendations:
        print(rec)
        print()

    # Create detailed report
    print("=" * 70)
    print("EXPORTING ANALYSIS")
    print("=" * 70)
    print()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = OUTPUT_DIR / "FAILURE_ANALYSIS_REPORT.md"
    create_detailed_report(analysis, report_path)

    # Export data
    export_analysis_data(analysis, OUTPUT_DIR)

    print()
    print("=" * 70)
    print("✅ ANALYSIS COMPLETE")
    print("=" * 70)
    print()
    print(f"📁 All outputs saved to: {OUTPUT_DIR.absolute()}")
    print()
    print("Next steps:")
    print("1. Review the detailed report for specific recommendations")
    print("2. Check the CSV files for data analysis")
    print("3. Implement the suggested fixes in the parsing pipeline")

