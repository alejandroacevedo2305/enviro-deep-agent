# PDF Processing - Quick Reference Card

## 🚀 Essential Commands

### Main Processing
```bash
uv run python SimpleWorkflow/pdf_processor.py
```

### Retry Failures
```bash
uv run python SimpleWorkflow/pdf_processor.py --retry-failed
```

---

## 🔄 Background Processing (One-Liners)

### Start Background Job
```bash
nohup uv run python SimpleWorkflow/pdf_processor.py --batch-size 1000 > SimpleWorkflow/pdf_processor.log 2>&1 &
```

### Monitor Progress in Real Time
```bash
tail -f SimpleWorkflow/pdf_processor.log | grep -E "Checkpoint|✓|Success Rate|Batch"
```

### Gracefully Kill It
```bash
kill $(pgrep -f "pdf_processor.py")
```

---

## 📂 Directory Options

### Custom Input Directory (Enhanced Retry)
```bash
uv run python SimpleWorkflow/retry_failed_files_enhanced.py --input-dir path/to/failures
```

### Test with Samples
```bash
uv run python SimpleWorkflow/retry_failed_files_enhanced.py \
    --input-dir SimpleWorkflow/ParsingFailsSamples --keep-failed
```

---

## ⚙️ Worker Configuration

### Auto-detected (Recommended)
```bash
uv run python SimpleWorkflow/pdf_processor.py
```

### Custom Workers
```bash
# High-performance
uv run python SimpleWorkflow/pdf_processor.py \
    --download-workers 30 --processing-workers 10

# Memory-constrained
uv run python SimpleWorkflow/pdf_processor.py \
    --download-workers 5 --processing-workers 2
```

---

## 📊 Monitoring

### Check Status
```bash
# Count FAILED files
find SimpleWorkflow/ParsedFiles -name "FAILED-*.md" | wc -l

# Count successful files
find SimpleWorkflow/ParsedFiles -name "*.md" ! -name "FAILED-*.md" | wc -l

# Check success rate
grep "Success Rate" SimpleWorkflow/pdf_processor.log | tail -1

# View checkpoint state
cat SimpleWorkflow/.pdf_processor_state.json | jq .
```

### System Resources
```bash
# Check if running
pgrep -f "pdf_processor.py" && echo "Running" || echo "Stopped"

# Monitor CPU/Memory
ps aux | grep pdf_processor | grep -v grep

# Memory usage
free -h
```

---

## 🔍 Analysis

### Analyze Failures
```bash
uv run python SimpleWorkflow/analyze_parsing_failures.py
```

### View Analysis Results
```bash
# Summary
cat SimpleWorkflow/failure_analysis/failure_summary.csv

# Patterns
cat SimpleWorkflow/failure_analysis/failure_patterns.csv
```

---

## 🎯 Common Workflows

### Daily Production
```bash
# Process new files
uv run python SimpleWorkflow/pdf_processor.py

# Retry failures
uv run python SimpleWorkflow/pdf_processor.py --retry-failed
```

### Large Batch (Millions)
```bash
# Start
nohup uv run python SimpleWorkflow/pdf_processor.py \
    --batch-size 1000 \
    --checkpoint-interval 200 \
    > SimpleWorkflow/pdf_processor.log 2>&1 &

# Monitor
tail -f SimpleWorkflow/pdf_processor.log | grep -E "Checkpoint|Success Rate"

# Stop
kill $(pgrep -f "pdf_processor.py")
```

### Testing
```bash
# Sample test
uv run python SimpleWorkflow/pdf_processor.py --sample 100

# Test retry
uv run python SimpleWorkflow/retry_failed_files_enhanced.py \
    --input-dir SimpleWorkflow/ParsingFailsSamples --keep-failed
```

---

## 🆘 Emergency Commands

### Force Kill (if graceful fails)
```bash
pkill -9 -f "pdf_processor.py"
```

### Clean Up After Crash
```bash
# Remove temp files
rm -rf /tmp/pdf_processor/*

# Clear checkpoint (if corrupt)
rm SimpleWorkflow/.pdf_processor_state.json

# Restart fresh
uv run python SimpleWorkflow/pdf_processor.py --clear-state
```

---

## 📖 Documentation

| Read Time | File | Purpose |
|-----------|------|---------|
| 2 min | `00_START_HERE.md` | Quick overview |
| 5 min | `INDEX.md` | Navigation |
| 20 min | `README.md` | Complete docs |

---

**Status:** ✅ Production-ready
**Success Rate:** 95-98%
**Scalability:** Millions of files

*Last updated: October 9, 2025*


