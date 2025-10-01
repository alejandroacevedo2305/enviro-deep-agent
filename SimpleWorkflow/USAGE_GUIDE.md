# Quick Usage Guide for Robust PDF Processing

## ✅ Problem Solved!

The original script was timing out on Linux. This new robust version solves that with:
- **Timeout protection** for each PDF file
- **Signal handling** for graceful shutdown
- **Resume capability** if interrupted
- **Background execution** that survives terminal closure

## 🚀 Quick Start

### Option 1: Background Mode (Recommended for All Files)

Process all files in the background:

```bash
# Run without max-files to process ALL rows
./SimpleWorkflow/run_processing.sh --mode background

# Monitor progress in real-time
tail -f SimpleWorkflow/processing_robust.log

# Check how many files have been processed
ls SimpleWorkflow/ParsedFiles/*.md | grep -v FAILED | wc -l

# Check processing state
cat SimpleWorkflow/.processing_state.json
```

### Option 2: Direct Command with Resume

```bash
# Start processing (Ctrl+C is safe - saves state)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py

# If interrupted, resume from where you left off
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --resume
```

### Option 3: Install Screen (for detachable sessions)

```bash
# Install screen
sudo apt-get install screen

# Run in screen session
./SimpleWorkflow/run_processing.sh --mode screen

# Detach: Press Ctrl+A, then D
# Reattach later: screen -r pdf_processing
```

## 📊 Monitoring Your Processing

### Real-Time Log Monitoring
```bash
# Watch the log as files are processed
tail -f SimpleWorkflow/processing_robust.log

# Or for specific log file
tail -f SimpleWorkflow/processing_*.log
```

### Check Progress
```bash
# Total processed files
ls SimpleWorkflow/ParsedFiles/*.md | grep -v FAILED | wc -l

# Total failed files
ls SimpleWorkflow/ParsedFiles/FAILED-*.md 2>/dev/null | wc -l

# View processing state (shows current progress)
cat SimpleWorkflow/.processing_state.json | python3 -m json.tool

# Check if process is still running
./SimpleWorkflow/run_processing.sh --status

# Or manually check
ps aux | grep sql_metadata_to_parsed_markdown
```

### System Resources
```bash
# Watch memory and CPU usage
htop

# Or simpler
top -p $(cat SimpleWorkflow/.processing.pid 2>/dev/null || echo "0")
```

## 🛑 Stopping the Process

### Graceful Shutdown (Saves Progress)
```bash
# If you know the PID
kill -TERM <PID>

# Or if running in background
PID=$(cat SimpleWorkflow/.processing.pid 2>/dev/null)
kill -TERM $PID

# The process will:
# 1. Finish the current file
# 2. Save the state
# 3. Exit gracefully
```

### Force Stop (Not Recommended)
```bash
kill -9 <PID>  # Use only if graceful shutdown doesn't work
```

## 🔄 Resuming After Interruption

If the process was interrupted (Ctrl+C, system reboot, etc.):

```bash
# Resume from where you left off
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --resume

# Or in background mode
./SimpleWorkflow/run_processing.sh --mode background --resume
```

## ⚙️ Advanced Options

### Custom Timeout
```bash
# Increase timeout to 10 minutes per file
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --timeout 600
```

### Memory Management
```bash
# Lower memory threshold for garbage collection (useful on low-RAM systems)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --memory-limit 2000
```

### Process Specific Files
```bash
# Process first 100 files
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --max-files 100

# Then process next 100 using skip-existing (automatic)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --max-files 200
```

## 📈 Expected Performance

- **Speed**: ~0.5-2 files/second (depends on PDF size and complexity)
- **Memory**: ~500-2000 MB typical usage
- **Timeout**: 5 minutes per file (adjustable)
- **Error Recovery**: Automatic with detailed error reports

## 🔍 Troubleshooting

### Script Still Timing Out?
```bash
# Increase the per-file timeout
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --timeout 900
```

### High Memory Usage?
```bash
# Process in smaller batches
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --max-files 1000
# Then run again (skip-existing is default)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --max-files 2000
```

### Many Failed Files?
```bash
# Check error reports
ls SimpleWorkflow/ParsedFiles/FAILED-*.md

# View a specific error
cat SimpleWorkflow/ParsedFiles/FAILED-<file_id>.md | head -n 50

# Common issues are in the error report
```

## 📝 Examples

### Example 1: Process Everything (Most Common)
```bash
# Start in background
./SimpleWorkflow/run_processing.sh --mode background

# Check after a few hours
ls SimpleWorkflow/ParsedFiles/*.md | grep -v FAILED | wc -l
```

### Example 2: Test with Small Batch First
```bash
# Test with 50 files
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --max-files 50

# If successful, process all
./SimpleWorkflow/run_processing.sh --mode background
```

### Example 3: Process Large Dataset Over Multiple Days
```bash
# Day 1: Process first 10,000
./SimpleWorkflow/run_processing.sh --mode background --max-files 10000

# Day 2: Process next 10,000 (automatically skips existing)
./SimpleWorkflow/run_processing.sh --mode background --max-files 20000

# Continue until all processed...
```

### Example 4: Recover from Interruption
```bash
# Your processing was interrupted...
# Check what was completed
cat SimpleWorkflow/.processing_state.json

# Resume
./SimpleWorkflow/run_processing.sh --mode background --resume
```

## 💡 Best Practices

1. **Start with background mode** - Survives terminal closure
2. **Monitor logs** - Use `tail -f` to watch progress
3. **Check progress regularly** - Count processed files
4. **Don't force kill** - Use graceful shutdown (SIGTERM)
5. **Resume capability** - It's safe to stop and resume anytime

## 🎯 For Your Use Case

To process all rows without timing out:

```bash
# Recommended: Run in background
./SimpleWorkflow/run_processing.sh --mode background

# This will:
# - Process ALL rows in metadata (182,406 files)
# - Skip already processed files automatically
# - Run in background (won't stop if terminal closes)
# - Save state for resume if needed
# - Log everything to processing_*.log

# Monitor with:
tail -f SimpleWorkflow/processing_*.log
```

That's it! Your files will process to completion without timeout issues.
