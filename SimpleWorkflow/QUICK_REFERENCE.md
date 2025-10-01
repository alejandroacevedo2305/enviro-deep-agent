# Quick Reference Card - PDF Processing

## 🚀 Quick Start (Choose One)

```bash
# 1. Best Performance (Recommended)
uv run python SimpleWorkflow/benchmark_workers.py --sample 50
# Then use the recommended settings

# 2. Auto-Optimized (No benchmark needed)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py

# 3. Reliable for Long Runs
./SimpleWorkflow/run_processing.sh --mode background
```

## 🛑 Stop Processing (Gracefully)

```bash
# Kill by PID file (safest)
kill -TERM $(cat SimpleWorkflow/.processing.pid 2>/dev/null)
kill -TERM $(cat SimpleWorkflow/.optimized.pid 2>/dev/null)

# Or by process name
pkill -TERM -f "sql_metadata_to_parsed_markdown"

# In terminal: Ctrl+C
```

## 📊 Monitor Progress

```bash
# Watch logs live
tail -f SimpleWorkflow/processing_*.log

# Count processed files
ls SimpleWorkflow/ParsedFiles/*.md | grep -v FAILED | wc -l

# Count failed files
ls SimpleWorkflow/ParsedFiles/FAILED-*.md 2>/dev/null | wc -l

# Check memory usage
ps aux | grep sql_metadata | awk '{print $6/1024 " MB"}'
```

## ⚡ Performance Quick Reference

| Your System | Command |
|-------------|---------|
| **4 CPU, 8GB RAM** | `--download-workers 8 --processing-workers 2` |
| **8 CPU, 16GB RAM** | `--download-workers 15 --processing-workers 4` |
| **16 CPU, 32GB RAM** | `--download-workers 20 --processing-workers 5` |

## 🔧 Common Commands

```bash
# Process all files (optimized)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py

# Process first 100 files
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py --max-files 100

# Background with custom workers
nohup uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py \
  --download-workers 15 --processing-workers 4 \
  > SimpleWorkflow/optimized.log 2>&1 &
echo $! > SimpleWorkflow/.optimized.pid

# Resume after interruption (robust version only)
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py --resume
```

## 🐛 Troubleshooting

```bash
# Script stuck? Check logs
tail -n 50 SimpleWorkflow/processing_*.log

# High memory? Lower workers
# Use: --download-workers 5 --processing-workers 2

# Slow network? Lower download workers
# Use: --download-workers 8

# Check for errors
ls SimpleWorkflow/ParsedFiles/FAILED-*.md | head -n 5
cat SimpleWorkflow/ParsedFiles/FAILED-<file>.md | head -n 30
```

## 📈 Expected Performance

- **Sync**: 0.5-2 files/second
- **Async**: 2-5 files/second
- **Robust**: 1-3 files/second
- **Optimized**: 5-15 files/second (after tuning)

## 🎯 Best Practices

1. **Always benchmark first**: `uv run python SimpleWorkflow/benchmark_workers.py --sample 50`
2. **Use graceful shutdown**: `kill -TERM` not `kill -9`
3. **Monitor resources**: Watch memory with `htop` or `top`
4. **Start conservative**: Begin with lower workers, increase gradually
5. **Check logs regularly**: `tail -f` to spot issues early

## 📞 Quick Help

- View this guide: `cat SimpleWorkflow/QUICK_REFERENCE.md`
- Full docs: `cat SimpleWorkflow/README.md`
- Usage guide: `cat SimpleWorkflow/USAGE_GUIDE.md`
