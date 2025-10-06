"""Summarize the outputs of the markdown files.

This script prints the total number of markdown files in
SimpleWorkflow/ParsedFiles, weight in MB, number of characters, and number of
words in the markdown files.

Run it using uv:

uv run python SimpleWorkflow/summarize_markdown_outputs.py
"""

# %%
from __future__ import annotations

import re
from pathlib import Path


def count_words(text: str) -> int:
    """Count words in text, excluding YAML frontmatter."""
    # Remove YAML frontmatter
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    # Split on whitespace and count non-empty tokens
    words = [w for w in text.split() if w.strip()]
    return len(words)


def parse_markdown_file(filepath: Path) -> dict:
    """Parse a single markdown file and return statistics."""
    try:
        content = filepath.read_text(encoding="utf-8")
        size_bytes = filepath.stat().st_size

        return {
            "filename": filepath.name,
            "size_bytes": size_bytes,
            "chars": len(content),
            "words": count_words(content),
            "lines": content.count("\n") + 1,
            "success": True,
            "error": None,
        }
    except Exception as e:
        return {
            "filename": filepath.name,
            "size_bytes": 0,
            "chars": 0,
            "words": 0,
            "lines": 0,
            "success": False,
            "error": str(e),
        }


def summarize_markdown_outputs(output_dir: Path = None) -> dict:
    """Summarize all markdown files in the output directory."""
    if output_dir is None:
        output_dir = Path("SimpleWorkflow/ParsedFiles")

    if not output_dir.exists():
        print(f"Error: Directory {output_dir} does not exist")
        return {}

    # Find all markdown files
    all_markdown = list(output_dir.glob("*.md"))
    success_files = [f for f in all_markdown if not f.name.startswith("FAILED-")]
    failed_files = [f for f in all_markdown if f.name.startswith("FAILED-")]

    # Collect statistics
    total_size = 0
    total_chars = 0
    total_words = 0
    total_lines = 0
    parse_errors = 0

    success_stats = []
    failed_stats = []

    print("Analyzing markdown files...")

    # Process successful files
    for filepath in success_files:
        stats = parse_markdown_file(filepath)
        if stats["success"]:
            total_size += stats["size_bytes"]
            total_chars += stats["chars"]
            total_words += stats["words"]
            total_lines += stats["lines"]
            success_stats.append(stats)
        else:
            parse_errors += 1

    # Process failed files
    for filepath in failed_files:
        stats = parse_markdown_file(filepath)
        if stats["success"]:
            failed_stats.append(stats)

    # Calculate summary
    summary = {
        "total_files": len(all_markdown),
        "success_files": len(success_files),
        "failed_files": len(failed_files),
        "parse_errors": parse_errors,
        "total_size_bytes": total_size,
        "total_size_mb": total_size / (1024 * 1024),
        "total_size_gb": total_size / (1024 * 1024 * 1024),
        "total_chars": total_chars,
        "total_words": total_words,
        "total_lines": total_lines,
        "avg_size_kb": (
            (total_size / 1024) / len(success_files) if success_files else 0
        ),
        "avg_words": total_words / len(success_files) if success_files else 0,
        "avg_lines": total_lines / len(success_files) if success_files else 0,
        "file_details": success_stats,
        "failed_details": failed_stats,
    }

    return summary


def print_file_details(file_stats: list[dict], show_all: bool = False):
    """Print individual file statistics."""
    if not file_stats:
        return

    # Sort by word count (descending) for interesting view
    sorted_stats = sorted(file_stats, key=lambda x: x["words"], reverse=True)

    # Show top 10 by default, or all if requested
    display_stats = sorted_stats if show_all else sorted_stats[:10]

    print("\n" + "-" * 70)
    print("📄 Individual File Statistics:")
    print("-" * 70)
    print(f"{'Filename':<40} {'Size (KB)':>10} {'Words':>10} {'Lines':>8}")
    print("-" * 70)

    for stat in display_stats:
        filename = stat["filename"]
        if len(filename) > 37:
            filename = filename[:34] + "..."

        size_kb = stat["size_bytes"] / 1024
        words = stat["words"]
        lines = stat["lines"]

        print(f"{filename:<40} {size_kb:>10.1f} {words:>10,} {lines:>8,}")

    if not show_all and len(sorted_stats) > 10:
        print("-" * 70)
        print(f"Showing top 10 of {len(sorted_stats)} files. Use --verbose to see all.")


def print_line_count_distribution(summary: dict):
    """Print distribution of files by line count ranges (successful only)."""
    file_details = summary.get("file_details", [])
    if not file_details:
        return

    # Define ranges
    ranges = [
        (5000, float("inf"), "more than 5,000 lines"),
        (1000, 5000, "less than 5,000 and more than 1,000 lines"),
        (100, 1000, "less than 1,000 and more than 100 lines"),
        (10, 100, "less than 100 and more than 10 lines"),
        (1, 10, "less than 10 and more than 1 lines"),
    ]

    print("\n📏 Line Count Distribution (Successful files only):")
    for min_val, max_val, label in ranges:
        if max_val == float("inf"):
            count = sum(1 for f in file_details if f["lines"] >= min_val)
        else:
            count = sum(1 for f in file_details if min_val < f["lines"] <= max_val)
        print(f"  Files with {label}: {count:>5,}")


def print_summary(summary: dict, verbose: bool = False):
    """Print summary statistics in a formatted way."""
    if not summary:
        return

    print("\n" + "=" * 70)
    print("MARKDOWN FILES SUMMARY")
    print("=" * 70)

    # Calculate failure percentage
    total_files = summary.get("total_files", 0)
    failed_files = summary.get("failed_files", 0)
    failure_rate = (failed_files / total_files) * 100 if total_files > 0 else 0

    print("\n📊 File Counts:")
    print(f"  Total files:        {summary['total_files']:>10,}")
    print(f"  ✓ Successful:       {summary['success_files']:>10,}")
    print(f"  ✗ Failed (FAILED-): {summary['failed_files']:>10,}")
    print(f"  Failure rate:       {failure_rate:>10.2f}%")
    if summary["parse_errors"] > 0:
        print(f"  ⚠ Parse errors:     {summary['parse_errors']:>10,}")

    if summary["success_files"] > 0:
        print("\n💾 Storage:")
        print(f"  Total size:         {summary['total_size_mb']:>10.2f} MB")
        if summary["total_size_gb"] >= 1:
            print(f"                      {summary['total_size_gb']:>10.2f} GB")
        print(f"  Average size:       {summary['avg_size_kb']:>10.2f} KB/file")

        print("\n📝 Content Statistics:")
        print(f"  Total characters:   {summary['total_chars']:>10,}")
        print(f"  Total words:        {summary['total_words']:>10,}")
        print(f"  Total lines:        {summary['total_lines']:>10,}")

        print("\n📈 Averages per File:")
        print(f"  Words:              {summary['avg_words']:>10,.0f}")
        print(f"  Lines:              {summary['avg_lines']:>10,.0f}")

        # Calculate success rate
        success_rate = (
            (summary["success_files"] / summary["total_files"]) * 100
            if summary["total_files"] > 0
            else 0
        )
        print(f"\n✨ Success Rate:      {success_rate:>10.1f}%")

        # Print line count distribution
        print_line_count_distribution(summary)

        # Print individual file details only in verbose mode
        if verbose:
            print_file_details(summary.get("file_details", []), show_all=verbose)

        # Show failed files if any
        if summary["failed_files"] > 0:
            print("\n" + "-" * 70)
            print("❌ Failed Files:")
            print("-" * 70)
            for stat in summary.get("failed_details", []):
                print(f"  • {stat['filename']}")

    print("=" * 70 + "\n")


def main():
    """Entry point for the summarization script."""
    import argparse

    parser = argparse.ArgumentParser(description="Summarize markdown output statistics")
    parser.add_argument(
        "--dir",
        type=Path,
        default=Path("SimpleWorkflow/ParsedFiles"),
        help="Directory containing markdown files (default: SimpleWorkflow/ParsedFiles)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output summary as JSON",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show all files (not just top 10)",
    )

    args = parser.parse_args()

    # Generate summary
    summary = summarize_markdown_outputs(args.dir)

    if not summary:
        return 1

    # Output results
    if args.json:
        import json

        print(json.dumps(summary, indent=2))
    else:
        print_summary(summary, verbose=args.verbose)

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
