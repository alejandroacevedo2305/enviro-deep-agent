# SimpleWorkflow: PDF to Markdown Processing Pipeline

Optimized asynchronous pipeline for downloading PDFs from S3 and converting
them to structured Markdown files with metadata extraction.

## Overview

SimpleWorkflow processes environmental assessment PDFs (flora/fauna reports)
from S3 storage, converts them to Markdown format, and enriches them with
metadata headers. The system uses advanced parallelization with separate
worker pools for I/O-bound downloads and CPU-intensive PDF parsing.

## Features

- **Dual Worker Pools**: Separate semaphores for downloads and processing
- **Auto-scaling**: Detects optimal worker configuration based on system
  resources
- **Connection Pooling**: Efficient S3 operations with aioboto3
- **Performance Metrics**: Tracks throughput, memory usage, and timing
- **Smart Skipping**: Avoids reprocessing existing files
- **Error Handling**: Robust retry logic with detailed error reports
- **Progress Tracking**: Real-time progress bars and logging

## Quick Start

### 1. Find Optimal Configuration

Before processing the full dataset, benchmark your system to find the best
worker configuration:

```bash
uv run python SimpleWorkflow/benchmark_workers.py --sample 50
```

This tests different worker combinations and recommends optimal settings for
your hardware and network conditions.

### 2. Run Processing

Use the recommended configuration from the benchmark:

```bash
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --download-workers 15 \
  --processing-workers 4
```

### 3. Run in Background

For long-running jobs, run in background with nohup:

```bash
nohup uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --download-workers 15 \
  --processing-workers 4 \
  > SimpleWorkflow/optimized_processing.log 2>&1 &
```

Save the process ID for later management:

```bash
echo $! > SimpleWorkflow/.optimized.pid
```

Monitor progress in real-time:

```bash
tail -f SimpleWorkflow/optimized_processing.log
```

Stop the background process:

```bash
kill $(cat SimpleWorkflow/.optimized.pid)
```

## Command Reference

### Retry Failed Files Script

High-performance retry script for failed PDF parsing with configurable
parallelism:

```bash
uv run python SimpleWorkflow/retry_failed_files.py \
  --download-workers 15 \
  --processing-workers 4
```

**Key Features:**
- Auto-detects optimal workers based on system resources
- Separate semaphores for download vs processing operations
- Performance metrics tracking (throughput, memory, speed)
- Memory-aware task scheduling with periodic garbage collection
- Handles UTF-8 BOM and corrupted files automatically
- Removes FAILED-*.md files after successful parsing

**Command-line Options:**
- `--download-workers N`: Number of concurrent download workers (default:
  auto-detected)
- `--processing-workers N`: Number of concurrent processing workers (default:
  auto-detected)

**Example with custom workers:**
```bash
uv run python SimpleWorkflow/retry_failed_files.py \
  --download-workers 20 \
  --processing-workers 6
```

**Run in background:**
```bash
nohup uv run python SimpleWorkflow/retry_failed_files.py \
  --download-workers 15 \
  --processing-workers 4 \
  > SimpleWorkflow/retry_processing.log 2>&1 &
```

Save the process ID for later management:

```bash
echo $! > SimpleWorkflow/.retry.pid
```

Monitor progress in real-time:

```bash
tail -f SimpleWorkflow/retry_processing.log
```

**Gracefully stop the background process:**

```bash
kill $(cat SimpleWorkflow/.retry.pid)
```

The script handles SIGTERM signals gracefully, completing current tasks before
exiting. For immediate termination (not recommended):

```bash
kill -9 $(cat SimpleWorkflow/.retry.pid)
```

### Main Processing Script

**File**: `sql_metadata_to_parsed_markdown_optimized.py`

```bash
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  [OPTIONS]
```

**Options:**

- `--download-workers N`: Number of concurrent S3 downloads (default: auto)
- `--processing-workers N`: Number of concurrent PDF parsers (default: auto)
- `--max-files N`: Process only first N files (useful for testing)
- `--skip-existing`: Skip files already processed (default: true)

**Examples:**

```bash
# Process first 100 files for testing
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --max-files 100

# Process all files with custom workers
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --download-workers 20 \
  --processing-workers 6

# Reprocess everything (ignore existing)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --skip-existing false
```

### Benchmark Script

**File**: `benchmark_workers.py`

```bash
uv run python SimpleWorkflow/benchmark_workers.py [OPTIONS]
```

**Options:**

- `--sample N`: Number of files to test per configuration (default: 50)

**Example:**

```bash
# Quick benchmark with 25 files per config
uv run python SimpleWorkflow/benchmark_workers.py --sample 25

# Thorough benchmark with 100 files per config
uv run python SimpleWorkflow/benchmark_workers.py --sample 100
```

### Summary Script

**File**: `summarize_markdown_outputs.py`

```bash
uv run python SimpleWorkflow/summarize_markdown_outputs.py
```

Displays statistics about processed files:

- Total number of markdown files
- Total size in MB
- Total characters and words

## Directory Structure

```
SimpleWorkflow/
├── README.md                              # This file
├── benchmark_workers.py                   # Worker config optimizer
├── sql_metadata_to_parsed_markdown_optimized.py  # Main processor
├── summarize_markdown_outputs.py          # Output statistics
├── ParsedFiles/                           # Output directory
│   ├── {file_id}.md                       # Successful conversions
│   └── FAILED-{file_id}.md                # Error reports
└── *.log                                  # Processing logs
```

## Input/Output

### Input

**Metadata File**: `sql/metadata_table/flora_fauna_metadata_indexed.parquet`

Required columns:

- `nombre`: Project name
- `fecha_de_presentacion`: Submission date
- `region`: Geographic region
- `tipo_de_proyecto`: Project type
- `url` or `bucket_name`/`key`: S3 location
- `from_compressed_file`: Boolean, if PDF is in ZIP

### Output

**Markdown Files**: `SimpleWorkflow/ParsedFiles/{file_id}.md`

Each markdown file includes:

1. **YAML Frontmatter**: Metadata header with file info
2. **Markdown Content**: Extracted and cleaned text from PDF

Example:

```markdown
---
file_identifier: 12345
s3_key: path/to/file.pdf
nombre: Project Name
fecha_presentacion: 2024-01-15
region: Region XV
tipo_proyecto: Mining
extraction_quality: high
page_count: 150
---

# Extracted Content

Document text here...
```

## Performance Tuning

### Worker Configuration

The system uses two worker pools:

1. **Download Workers** (I/O-bound):
   - Default: 3x CPU cores, capped at 20
   - Higher is better for network-heavy workloads
   - Limited by memory (each worker uses ~50-100 MB)

2. **Processing Workers** (CPU-bound):
   - Default: CPU cores - 1, capped at 10
   - Limited by CPU and memory (each worker uses ~200-500 MB)
   - PDF parsing is CPU-intensive

### Recommended Configurations

**Small System** (4 cores, 8GB RAM):

```bash
--download-workers 8 --processing-workers 3
```

**Medium System** (8 cores, 16GB RAM):

```bash
--download-workers 15 --processing-workers 6
```

**Large System** (16+ cores, 32GB+ RAM):

```bash
--download-workers 20 --processing-workers 10
```

### Monitoring

Watch key metrics during processing:

- **Throughput**: Files processed per second
- **Memory**: Peak memory usage (should stay under 80% of total RAM)
- **Download Speed**: MB/s from S3
- **Avg Times**: Download vs processing time balance

If downloads are slower than processing, increase download workers. If
processing is slower, increase processing workers (if you have CPU/memory
headroom).

## Troubleshooting

### Common Issues

**Out of Memory:**

- Reduce processing workers
- Reduce download workers
- Add more RAM or enable swap

**Slow Processing:**

- Run benchmark to find optimal configuration
- Check network speed to S3
- Ensure CPU isn't throttling (check temperatures)

**High Failure Rate:**

- Check S3 credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
- Verify bucket permissions
- Inspect FAILED-*.md files for error details

**No Progress:**

- Check logs in SimpleWorkflow/*.log
- Verify metadata file exists and has correct format
- Test with --max-files 10 first

## Advanced Usage

### Running Multiple Instances

Process different subsets in parallel:

```bash
# Terminal 1: Process first half
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --max-files 5000 > processing_1.log 2>&1 &

# Terminal 2: Process second half (modify script to skip first 5000)
# Note: Requires code modification to support offset parameter
```

### Custom Metadata

Modify the script to add custom metadata fields to the YAML frontmatter. See
lines 287-296 in `sql_metadata_to_parsed_markdown_optimized.py`.

### Integration with Airflow

This workflow can be integrated into Airflow DAGs. See the parent `dags/`
directory for examples of Airflow integration patterns.

## Environment Variables

Required:

- `AWS_ACCESS_KEY_ID`: S3 access key
- `AWS_SECRET_ACCESS_KEY`: S3 secret key

Optional:

- `AWS_DEFAULT_REGION`: S3 region (default: us-east-1)
- `AWS_ENDPOINT_URL`: Custom S3 endpoint for non-AWS providers

## Dependencies

Core dependencies (managed by uv):

- `pandas`: Metadata handling
- `aioboto3`: Async S3 operations
- `psutil`: System resource monitoring
- `tqdm`: Progress bars
- `python-dotenv`: Environment configuration

PDF processing (from parent project):

- `localPDFparse`: PDF extraction engine
- `s3pdf_manager`: S3 utilities

## Performance Expectations

Typical throughput (varies by system and network):

- **Small PDFs** (<5 MB, <50 pages): 2-5 files/second
- **Medium PDFs** (5-20 MB, 50-200 pages): 0.5-2 files/second
- **Large PDFs** (>20 MB, >200 pages): 0.2-0.5 files/second

For a dataset of 10,000 files averaging 10 MB each:

- **Processing Time**: 1-3 hours (depending on configuration)
- **Network Usage**: ~100 GB download
- **Disk Space**: ~5-10 GB for markdown outputs
- **Memory**: 2-8 GB peak usage

## License & Credits

Part of the NVIRO Airflow parsing pipeline for environmental document
processing. See parent repository for full context.
