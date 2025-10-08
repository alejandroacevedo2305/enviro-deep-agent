# Retry Failed Files Optimizer Guide

## Overview

The `optimize_retry_workers.py` script helps you find the optimal worker
configuration for `retry_failed_files.py` on your specific machine and network
conditions.

## Why Use the Optimizer?

The retry script has two key parameters that significantly affect performance:
- **Download workers**: Controls concurrent S3 downloads (I/O-bound)
- **Processing workers**: Controls concurrent PDF parsing (CPU/memory-bound)

The optimal values depend on:
- CPU cores and speed
- Available RAM
- Network bandwidth to S3
- PDF complexity

The optimizer tests different combinations to find the sweet spot for your
system.

## How It Works

The optimizer:

1. **Scans for failed files** in `SimpleWorkflow/ParsedFiles/`
2. **Samples a subset** (default 30 files) for testing
3. **Tests multiple configurations** from conservative to aggressive:
   - Conservative: `(5, 2)` - safe for most systems
   - Balanced: `(10, 3)`, `(15, 4)` - good starting points
   - Aggressive: `(20, 5)`, `(25, 6)` - for powerful systems
   - Specialized: I/O-heavy vs CPU-heavy variants
4. **Measures performance** for each configuration:
   - Throughput (files/sec)
   - Memory usage
   - Download speeds
   - Processing times
5. **Ranks configurations** by throughput
6. **Provides optimal command** ready to run

**Important**: The optimizer runs in **dry-run mode** - it downloads and
processes files but doesn't modify any FAILED-*.md files. This is purely for
benchmarking.

## Usage

### Basic Usage

```bash
uv run python SimpleWorkflow/optimize_retry_workers.py
```

This tests with 30 files per configuration (good balance of speed vs accuracy).

### Test with More Files

For more accurate results (but slower):

```bash
uv run python SimpleWorkflow/optimize_retry_workers.py --sample 50
```

### Custom Memory Threshold

Stop tests that exceed a memory percentage (default 80%):

```bash
uv run python SimpleWorkflow/optimize_retry_workers.py --max-memory 75
```

## Example Output

```
======================================================================
RETRY FAILED FILES - WORKER OPTIMIZATION
======================================================================

System Information:
  CPUs: 20
  RAM: 125.8 GB
  Max memory threshold: 80.0%

Scanning for failed files...
Found 127 failed files
Will test with 30 files per configuration

Loading metadata...
✓ Loaded metadata with 15420 rows

Testing 12 configurations...

======================================================================
Testing: 5 download workers, 2 processing workers
✓ Result: 1.23 files/sec | Peak memory: 854 MB
======================================================================
Testing: 10 download workers, 3 processing workers
✓ Result: 2.01 files/sec | Peak memory: 1243 MB
======================================================================
Testing: 20 download workers, 5 processing workers
✓ Result: 2.45 files/sec | Peak memory: 1876 MB
...

======================================================================
OPTIMIZATION RESULTS
======================================================================

#1 Configuration:
  Download workers: 20
  Processing workers: 5
  Throughput: 2.45 files/sec
  Total time: 12.2s
  Success rate: 30/30
  Avg download: 0.82s
  Avg processing: 3.14s
  Peak memory: 1876 MB
  Download speed: 4.23 MB/s

#2 Configuration:
  Download workers: 15
  Processing workers: 4
  Throughput: 2.31 files/sec
  Total time: 13.0s
  Success rate: 30/30
  Avg download: 0.95s
  Avg processing: 3.21s
  Peak memory: 1502 MB
  Download speed: 3.89 MB/s

...

======================================================================
RECOMMENDATION
======================================================================

✓ Optimal configuration found:
  Download workers: 20
  Processing workers: 5
  Expected throughput: 2.45 files/sec
  Estimated time for 127 failed files: 0.9 minutes

Recommended command:
  uv run python SimpleWorkflow/retry_failed_files.py \
    --download-workers 20 \
    --processing-workers 5

Or run in background:
  nohup uv run python SimpleWorkflow/retry_failed_files.py \
    --download-workers 20 \
    --processing-workers 5 \
    > SimpleWorkflow/retry_processing.log 2>&1 &
======================================================================
```

## Understanding the Results

### Key Metrics

- **Throughput**: Files processed per second (higher is better)
- **Peak memory**: Maximum RAM used during processing
- **Avg download time**: Time to download each PDF from S3
- **Avg processing time**: Time to convert PDF to markdown
- **Download speed**: Network throughput from S3

### Choosing a Configuration

The optimizer ranks by throughput, but consider:

1. **Memory constraints**: If peak memory is close to your system's limit,
   choose a less aggressive configuration
2. **Stability**: The #2 or #3 configuration might be more stable than #1
3. **Other workloads**: If running other tasks, use fewer workers

### Common Patterns

- **Network-bound**: High download times → increase download workers
- **CPU-bound**: High processing times → increase processing workers
- **Memory-bound**: Peak memory near limit → reduce both workers
- **Balanced**: Download and processing times similar → current config is good

## Tips

1. **Run during normal conditions**: Network and system load affect results
2. **Test with realistic samples**: Default 30 files is usually sufficient
3. **Re-run periodically**: Optimal config may change with PDF complexity
4. **Start conservative**: If unsure, use top-3 configuration instead of #1
5. **Monitor during production**: Watch logs to ensure chosen config is stable

## Troubleshooting

### No Failed Files Found

```
Error: No failed files found to optimize with!
```

**Solution**: Run the main processing script first to generate some failed
files, then retry the optimizer.

### Memory Exceeded Warning

```
Memory usage exceeded 80.0% threshold
```

**Solution**: This configuration uses too much RAM. The optimizer will skip it
and try others. You can:
- Increase `--max-memory` if you know your system can handle it
- Accept that your system can't handle aggressive configurations

### All Configurations Failed

**Check**:
- S3 credentials are configured correctly (`.env` file)
- Network connection to S3 is working
- Failed file metadata is valid

## Advanced Usage

### Testing Specific Configurations

If you want to test specific worker counts, you can modify the script's
`generate_test_configurations()` function or run manual tests with
`retry_failed_files.py` directly.

### Interpreting Logs

The optimizer logs to:
- **Console**: Summary results
- **File**: `SimpleWorkflow/optimize_retry_workers.log` (detailed logs)

Review the log file for detailed timing information on each configuration.

## Next Steps

After running the optimizer:

1. **Copy the recommended command** from the output
2. **Test it** with a small batch first (it will process all failed files)
3. **Run in background** for large batches using `nohup`
4. **Monitor progress** with `tail -f SimpleWorkflow/retry_processing.log`

## Integration with Workflow

Recommended workflow:

```bash
# Step 1: Run main processing (generates failed files)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py

# Step 2: Optimize retry configuration
uv run python SimpleWorkflow/optimize_retry_workers.py

# Step 3: Run retry with optimal settings (from optimizer output)
uv run python SimpleWorkflow/retry_failed_files.py \
  --download-workers 20 \
  --processing-workers 5

# Step 4: Check results
ls -lh SimpleWorkflow/ParsedFiles/FAILED-*.md
```

## Performance Expectations

Typical throughput on different systems:

| System Type | CPUs | RAM | Expected Throughput |
|-------------|------|-----|---------------------|
| Small       | 4    | 8GB | 0.5-1.0 files/sec   |
| Medium      | 8    | 16GB| 1.0-2.0 files/sec   |
| Large       | 16   | 32GB| 2.0-3.5 files/sec   |
| Very Large  | 20+  | 64GB+| 3.0-5.0 files/sec  |

**Note**: Network bandwidth to S3 and PDF complexity are major factors.

## Configuration Limits

The optimizer automatically calculates safe limits based on:

- **Max download workers**: `min(CPU_count × 3, RAM_GB × 2, 30)`
- **Max processing workers**: `min(CPU_count - 1, RAM_GB / 2, 12)`

These ensure the system remains stable during benchmarking.

## FAQ

**Q: How long does optimization take?**
A: 5-15 minutes depending on number of configurations and sample size.

**Q: Can I run the optimizer multiple times?**
A: Yes, it's completely safe and doesn't modify files.

**Q: Should I re-run after system changes?**
A: Yes, if you upgrade hardware or change network conditions.

**Q: What if optimal config still seems slow?**
A: Check network bandwidth, PDF sizes, and consider profiling individual
operations.

**Q: Can I parallelize across multiple machines?**
A: Yes, but you'd need to partition the failed files list. The optimizer only
optimizes for a single machine.

