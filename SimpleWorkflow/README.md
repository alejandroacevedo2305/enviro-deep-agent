# SimpleWorkflow - PDF to Markdown Converter

A robust Python script that downloads PDFs from S3 and converts them to Markdown format for RAG (Retrieval-Augmented Generation) applications. Available in synchronous, asynchronous, and ultra-robust versions for different requirements and long-running tasks.

## 📋 Overview

This workflow processes PDF documents stored in AWS S3 by:
1. Reading metadata from a parquet file
2. Downloading PDFs from S3 (with automatic retry logic)
3. Converting PDFs to clean Markdown format
4. Saving processed files with metadata headers
5. Creating error reports for failed conversions

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- AWS credentials configured
- Required Python packages (installed automatically with uv)

### Environment Setup

1. Create a `.env` file in the project root with your AWS credentials:

```bash
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_DEFAULT_REGION=us-west-2
```

### Basic Usage

**Synchronous Version (Default):**
```bash
# Process all PDFs in the metadata
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py

# Process first 10 PDFs
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --max-files 10

# Process specific files by their identifiers
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --indices "file_id_1" "file_id_2"

# Process a random sample of 5 files
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --sample 5

# Dry run - see what would be processed without downloading
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --dry-run --max-files 20
```

**Async Parallel Version (For Better Performance):**
```bash
# Process with parallel downloads and parsing (5 workers by default)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py --max-files 100

# Process with custom number of parallel workers
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py --max-files 100 --workers 10

# Process sample with high concurrency
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py --sample 50 --workers 8
```

**Ultra-Robust Version (For Long-Running Tasks on Linux):**
```bash
# Process with timeout protection and signal handling
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --max-files 1000

# Resume from previous state after interruption
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --resume

# Run in background with nohup using wrapper script
./SimpleWorkflow/run_processing.sh --mode background --max-files 10000

# Run in screen session for detachable processing
./SimpleWorkflow/run_processing.sh --mode screen --max-files 10000

# Run in tmux session
./SimpleWorkflow/run_processing.sh --mode tmux

# Check status of background job
./SimpleWorkflow/run_processing.sh --status
```

**Optimized Async Version (Maximum Performance):**
```bash
# Benchmark to find optimal workers for your system
uv run python SimpleWorkflow/benchmark_workers.py --sample 50

# Run with auto-detected optimal settings
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py

# Run with custom worker configuration
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --download-workers 15 --processing-workers 4 --max-files 1000

# Background mode with optimal settings
nohup uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  > SimpleWorkflow/optimized_processing.log 2>&1 &

# Save PID for later
echo $! > SimpleWorkflow/.optimized.pid
```

## 📁 File Structure

```
SimpleWorkflow/
├── README.md                                    # This file
├── USAGE_GUIDE.md                               # Quick usage guide
├── sql_metadata_to_parsed_markdown.py           # Synchronous version
├── sql_metadata_to_parsed_markdown_async.py     # Async parallel version
├── sql_metadata_to_parsed_markdown_robust.py    # Ultra-robust with timeout
├── sql_metadata_to_parsed_markdown_optimized.py # Optimized async (best performance)
├── benchmark_workers.py                         # Find optimal worker settings
├── run_processing.sh                            # Wrapper script for background execution
├── ParsedFiles/                                 # Output directory
│   ├── {file_id}.md                            # Successfully processed files
│   └── FAILED-{file_id}.md                     # Error reports for failed files
├── .processing_state.json                       # State file for resume capability
├── .processing.pid                              # PID file for background jobs
├── .optimized.pid                               # PID for optimized version
├── processing.log                               # Processing logs (sync)
├── processing_async.log                         # Processing logs (async)
├── processing_robust.log                        # Processing logs (robust)
└── processing_optimized.log                     # Processing logs (optimized)
```

## ⚙️ Command Line Options

| Option | Description | Example | Available In |
|--------|-------------|---------|--------------|
| `--max-files N` | Process only N files | `--max-files 100` | All |
| `--indices ID1 ID2...` | Process specific file IDs | `--indices "2129356319_ei-document_"` | Sync/Async |
| `--sample N` | Process random sample of N files | `--sample 10` | Sync/Async |
| `--skip-existing` | Skip already processed files (default) | `--skip-existing` | All |
| `--no-skip-existing` | Reprocess all files | `--no-skip-existing` | All |
| `--dry-run` | Preview what would be processed | `--dry-run` | Sync/Async |
| `--workers N` | Number of parallel workers | `--workers 8` | Async only |
| `--retry-failed` | Retry only previously failed files | `--retry-failed` | Sync/Async |
| `--resume` | Resume from previous state | `--resume` | Robust only |
| `--timeout N` | Timeout per file in seconds | `--timeout 600` | Robust only |
| `--memory-limit N` | Memory limit in MB before GC | `--memory-limit 8000` | Robust only |
| `--download-workers N` | Number of download workers | `--download-workers 15` | Optimized only |
| `--processing-workers N` | Number of processing workers | `--processing-workers 4` | Optimized only |

## 📊 Output Format

### Successfully Processed Files

Each markdown file includes:
- **Metadata header** with file information
- **Clean markdown content** from the PDF
- **Preserved structure** (headings, tables, lists)

Example output structure:
```markdown
---
file_identifier: 2129356319_ei-document_
s3_key: sea-crawler/2129356319/ei-document/file.pdf
nombre: Project Name
fecha_presentacion: 2024-01-15
region: Región del Maule
extraction_quality: high
page_count: 45
---

# Document Content
...
```

### Failed Processing Reports

Error reports (`FAILED-{file_id}.md`) contain:
- Error type and message
- Full traceback for debugging
- Complete metadata information
- Suggested troubleshooting steps

## 🔍 Monitoring Progress

### Real-time Progress

The script provides comprehensive progress tracking:

**Initial Display:**
- Total rows in the metadata parquet file
- Number of files to be processed
- Column information from the metadata

**Dynamic Progress Bar:**
- Current file being processed (e.g., `[1/100]`)
- Percentage completed with visual bar
- Files per second processing rate
- Estimated time remaining
- Real-time counters:
  - ✓ Successfully processed files
  - ⏭ Skipped existing files
  - ✗ Failed files

### Log Files

Check `processing.log` for detailed information:
```bash
tail -f SimpleWorkflow/processing.log
```

### Processing Summary

Example output when starting:
```
============================================================
✓ Successfully loaded metadata
  Total rows in parquet file: 182,406
  Columns: id, url, nombre, fecha_de_presentacion, tipologia, ... (16 total)
============================================================
Total rows in metadata: 182,406
Files to process: 100
============================================================
```

During processing:
```
Processing [45/100]: 45%|████▌     | 45/100 [02:15<02:45, 3.01s/files] ✓35 ⏭8 ✗2
```

After completion:
```
Processing Summary:
  Total files: 100
  Processed: 85
  Skipped (existing): 10
  Failed: 5
```

## 🛠️ Troubleshooting

### Common Issues

1. **Authentication Error**
   - Check AWS credentials in `.env` file
   - Verify AWS_DEFAULT_REGION is set correctly

2. **File Not Found in S3**
   - Check if S3 bucket/key exists
   - Verify metadata is up-to-date

3. **PDF Conversion Failed**
   - Check FAILED-{file_id}.md for details
   - File might be corrupted or not a valid PDF

4. **Memory Issues with Large PDFs**
   - Process in smaller batches
   - Files over 100MB will show a warning
   - Use `--memory-limit` flag with robust version

5. **Script Timeout or Hanging on Linux**
   - Use the robust version: `sql_metadata_to_parsed_markdown_robust.py`
   - Run with wrapper script: `./SimpleWorkflow/run_processing.sh --mode background`
   - Adjust timeout: `--timeout 600` (10 minutes per file)
   - Resume after interruption: `--resume`

### Retry Failed Files

**New Method (Recommended):**
Use the `--retry-failed` flag to automatically retry only previously failed files:

```bash
# Retry failed files with sync version
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --retry-failed

# Retry failed files with async version (faster)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py --retry-failed --workers 5

# Preview what would be retried
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --retry-failed --dry-run
```

**Features of Retry Mode:**
- Automatically detects all FAILED-*.md files
- Only processes files that previously failed
- Removes FAILED-*.md files for successfully processed files
- Tracks retry attempts in error reports
- Works with both sync and async versions

**Manual Method (Alternative):**
```bash
# Remove specific error reports and retry
rm SimpleWorkflow/ParsedFiles/FAILED-*.md
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --skip-existing
```

## ⚡ Performance Comparison & Optimization

### Version Comparison

| Version | Best For | Pros | Cons | Typical Speed |
|---------|----------|------|------|---------------|
| **Sync** | Small batches (<50 files) | Simple, predictable, lower memory | Sequential, slower | 0.5-2 files/s |
| **Async** | Large batches (>50 files) | Parallel downloads | Higher memory, fixed workers | 2-5 files/s |
| **Robust** | Unattended long runs | Timeout protection, resume | Safety overhead | 1-3 files/s |
| **Optimized** | Maximum throughput | Best performance, auto-tuning | Requires tuning | 5-15 files/s |

### Finding Optimal Settings

The optimized version can achieve 3-5x better performance than the standard async version by separating download and processing workers.

**Step 1: Run Benchmark**

```bash
# Test with 50 random files to find best configuration for your system
uv run python SimpleWorkflow/benchmark_workers.py --sample 50
```

The benchmark will test multiple configurations and output:
- Throughput (files/second) for each configuration
- Memory usage patterns
- Recommended settings for your system

**Step 2: Use Recommended Settings**

After benchmarking, use the recommended configuration:

```bash
# Example output from benchmark:
# Recommended: --download-workers 15 --processing-workers 4

uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --download-workers 15 \
  --processing-workers 4
```

### Performance Tuning Guide

**System Resources:**
- **Low RAM (<8GB)**: Use `--download-workers 5 --processing-workers 2`
- **Medium RAM (8-16GB)**: Use `--download-workers 10 --processing-workers 3`
- **High RAM (16-32GB)**: Use `--download-workers 15 --processing-workers 4`
- **Very High RAM (>32GB)**: Use `--download-workers 20 --processing-workers 5`

**Network Speed:**
- **Slow (<10 Mbps)**: Lower download workers to 5-8
- **Fast (>50 Mbps)**: Increase download workers to 15-20

**CPU Cores:**
- Processing workers should be: `min(CPU_cores - 1, 5)`
- Download workers can be: `CPU_cores * 2 to 3`

### Real-World Performance Examples

```bash
# Conservative (4 CPU, 8GB RAM, slow network)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --download-workers 8 --processing-workers 2

# Balanced (8 CPU, 16GB RAM, good network)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --download-workers 15 --processing-workers 4

# Aggressive (16 CPU, 32GB RAM, fast network)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --download-workers 20 --processing-workers 5
```

### Recommended Settings

- **Small batches (1-50 files)**: Use sync version
  ```bash
  uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --max-files 50
  ```

- **Medium batches (50-500 files)**: Use async with moderate workers
  ```bash
  uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py --max-files 500 --workers 5
  ```

- **Large batches (500+ files)**: Use async with more workers
  ```bash
  uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py --max-files 1000 --workers 10
  ```

### Performance Benchmarks

Typical processing speeds (may vary based on PDF size and complexity):
- **Sync version**: ~0.5-2 files/second
- **Async version (5 workers)**: ~2-5 files/second
- **Async version (10 workers)**: ~3-8 files/second

## 🛑 Graceful Shutdown Commands

All scripts support graceful shutdown that saves progress and exits cleanly.

### Kill Background Jobs Gracefully

```bash
# Method 1: Using PID file (recommended)
kill -TERM $(cat SimpleWorkflow/.processing.pid 2>/dev/null)
# Or for optimized version
kill -TERM $(cat SimpleWorkflow/.optimized.pid 2>/dev/null)

# Method 2: Using wrapper script
./SimpleWorkflow/run_processing.sh --status  # Get PID first
kill -TERM <PID>

# Method 3: Find and kill by process name
pkill -TERM -f "sql_metadata_to_parsed_markdown"

# Specific version
pkill -TERM -f "sql_metadata_to_parsed_markdown_robust"
pkill -TERM -f "sql_metadata_to_parsed_markdown_optimized"
```

### Kill Foreground Process

```bash
# Press Ctrl+C in the terminal
# The script will:
# 1. Finish processing current file
# 2. Save state (if using robust version)
# 3. Log summary and exit gracefully
```

### Verify Process Was Killed

```bash
# Check if process is still running
ps aux | grep sql_metadata_to_parsed_markdown

# Check processing state
cat SimpleWorkflow/.processing_state.json

# View last log entries
tail -n 20 SimpleWorkflow/processing_*.log
```

### Force Kill (Use Only as Last Resort)

```bash
# Only if graceful shutdown fails after 30 seconds
kill -9 $(cat SimpleWorkflow/.processing.pid 2>/dev/null)

# Or by process name
pkill -9 -f "sql_metadata_to_parsed_markdown"

# Note: Force kill may leave incomplete files or unsaved state
```

### Clean Up After Shutdown

```bash
# Remove PID files
rm -f SimpleWorkflow/.processing.pid SimpleWorkflow/.optimized.pid

# Check for orphaned temp files
ls /tmp/pdf_processing*/ 2>/dev/null

# Clean up temp files if needed
rm -rf /tmp/pdf_processing*/
```

## 🔄 Handling Long-Running Processes

For processing thousands of files that may take hours or days:

### Using the Robust Version

```bash
# Start processing with resume capability
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --max-files 10000

# If interrupted, resume from where you left off
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --resume

# Monitor progress
cat SimpleWorkflow/.processing_state.json | jq '.'
```

### Using the Wrapper Script

```bash
# Run in background (survives terminal closure)
./SimpleWorkflow/run_processing.sh --mode background --max-files 10000

# Run in screen session (can detach/reattach)
./SimpleWorkflow/run_processing.sh --mode screen --max-files 10000

# Run in tmux session
./SimpleWorkflow/run_processing.sh --mode tmux --max-files 10000

# Check status
./SimpleWorkflow/run_processing.sh --status

# Monitor logs in real-time
tail -f SimpleWorkflow/processing_robust.log
```

### Monitoring Progress

```bash
# Count processed files
ls SimpleWorkflow/ParsedFiles/*.md | grep -v FAILED | wc -l

# Count failed files
ls SimpleWorkflow/ParsedFiles/FAILED-*.md 2>/dev/null | wc -l

# Check memory usage
ps aux | grep sql_metadata_to_parsed_markdown

# View processing state
cat SimpleWorkflow/.processing_state.json
```

### Graceful Shutdown

The robust version handles Linux signals properly:
- `Ctrl+C` or `kill -TERM <pid>`: Graceful shutdown, saves state
- State is preserved for resume
- No data loss on interruption

## 📈 Performance Tips

1. **Batch Processing**: Process files in batches to avoid overwhelming the system
   ```bash
   # Process in batches of 100
   uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --max-files 100
   ```

2. **Parallel Processing**: The script processes files sequentially for stability. For parallel processing, run multiple instances with different index ranges.

3. **Skip Existing**: Always use `--skip-existing` (default) to avoid reprocessing files

4. **Monitor Resources**: Watch system resources for large batches:
   ```bash
   htop  # or top
   ```

## 🔒 Safety Features

- **Automatic Retry**: Failed S3 downloads retry up to 3 times with exponential backoff
- **Error Recovery**: Failures don't stop the entire batch
- **Clean Temporary Files**: Automatically cleans up temp files
- **Skip System Files**: Ignores macOS system files (__MACOSX, ._ files)
- **Unicode Handling**: Safely handles problematic characters
- **Smart Retry System**:
  - Tracks failed files with detailed error reports
  - Automatic cleanup of error reports after successful retry
  - Prevents infinite retry loops
  - Maintains retry attempt history

## 📝 Examples

### Example 1: Initial Processing
```bash
# First, do a dry run to see what will be processed
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --dry-run --max-files 50

# Then process the files
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --max-files 50
```

### Example 2: Daily Processing
```bash
# Process new files only (skips existing)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py
```

### Example 3: Testing with Sample
```bash
# Test with 3 random files
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --sample 3
```

### Example 4: Reprocess Specific Files
```bash
# Force reprocess specific files
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py \
  --indices "2129356319_ei-document_" "2129370353_ei-document_" \
  --no-skip-existing
```

### Example 5: Complete Workflow with Retry
```bash
# Step 1: Initial processing batch
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py --max-files 1000 --workers 10

# Step 2: Check how many failed
ls SimpleWorkflow/ParsedFiles/FAILED-*.md | wc -l

# Step 3: Retry failed files
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py --retry-failed --workers 8

# Step 4: Check remaining failures (likely corrupted PDFs)
ls SimpleWorkflow/ParsedFiles/FAILED-*.md

# Step 5: Review specific error for investigation
head -n 30 SimpleWorkflow/ParsedFiles/FAILED-{specific_file}.md
```

## 📚 Additional Information

- **Input**: Reads from `sql/metadata_table/flora_fauna_metadata_indexed.parquet`
- **Output**: Saves to `SimpleWorkflow/ParsedFiles/`
- **Temp Files**: Uses system temp directory (`/tmp/pdf_processing/`)
- **Logs**: Writes to `SimpleWorkflow/processing.log`

## 🤝 Support

For issues or questions:
1. Check the error reports in `ParsedFiles/FAILED-*.md`
2. Review the `processing.log` file
3. Ensure AWS credentials are correctly configured
4. Verify the metadata parquet file is accessible

---

*This workflow is designed for reliable, production-ready PDF processing with comprehensive error handling and recovery mechanisms.*
