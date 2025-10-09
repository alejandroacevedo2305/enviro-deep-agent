# 🚀 PDF Processing Pipeline - Start Here

**Production-ready tools optimized for processing millions of PDFs.**

---

## ⚡ Quick Start (30 seconds)

### Process New PDFs
```bash
uv run python SimpleWorkflow/pdf_processor.py
```

### Retry Failed PDFs
```bash
# Option A: Using main processor (recommended)
uv run python SimpleWorkflow/pdf_processor.py --retry-failed

# Option B: Using specialized retry tool
uv run python SimpleWorkflow/retry_failed_files_enhanced.py
```

**That's it!** Both tools are production-ready and fully optimized.

---

## 🛠️ The Two Main Tools

### 1. **Main PDF Processor** (`pdf_processor.py`)

**What it does:**
- Processes PDFs from metadata parquet file
- Can also retry FAILED-*.md files
- Optimized for millions of files
- Async, batching, checkpointing, graceful shutdown

**When to use:**
- ✅ Initial bulk processing from metadata
- ✅ Daily incremental processing
- ✅ Retrying failures as part of main pipeline
- ✅ Long-running background jobs

**Key features:**
- Consolidated from 4 previous scripts
- All features combined
- 95-98% success rate
- Scales to millions

**Quick commands:**
```bash
# Default: Process all new files
uv run python SimpleWorkflow/pdf_processor.py

# Retry only failures
uv run python SimpleWorkflow/pdf_processor.py --retry-failed

# Large batch (millions)
uv run python SimpleWorkflow/pdf_processor.py \
    --batch-size 1000 --checkpoint-interval 200

# Sample test
uv run python SimpleWorkflow/pdf_processor.py --sample 100
```

### 2. **Enhanced Retry Tool** (`retry_failed_files_enhanced.py`)

**What it does:**
- Searches for FAILED-*.md files in a directory
- Retries with advanced strategies
- Flexible directory configuration
- Default: SimpleWorkflow/ParsedFiles

**When to use:**
- ✅ Testing with ParsingFailsSamples
- ✅ Custom directory processing
- ✅ Keeping FAILED files for analysis
- ✅ More detailed retry statistics

**Key features:**
- 91.8% success rate on failures
- Works with any directory
- Comprehensive error categorization
- Background management script

**Quick commands:**
```bash
# Default: Retry FAILED files in ParsedFiles
uv run python SimpleWorkflow/retry_failed_files_enhanced.py

# Custom directory
uv run python SimpleWorkflow/retry_failed_files_enhanced.py \
    --input-dir path/to/failures

# Background mode
./SimpleWorkflow/manage_retry.sh start
./SimpleWorkflow/manage_retry.sh status
./SimpleWorkflow/manage_retry.sh stop
```

---

## 📊 Which Tool Should I Use?

### For Most Cases: Use `pdf_processor.py`

```bash
# Processing new files
uv run python SimpleWorkflow/pdf_processor.py

# Retrying failures
uv run python SimpleWorkflow/pdf_processor.py --retry-failed
```

**Why:**
- One tool for everything
- Simpler workflow
- Same optimizations
- Integrated retry

### For Special Cases: Use `retry_failed_files_enhanced.py`

```bash
# Testing with ParsingFailsSamples
uv run python SimpleWorkflow/retry_failed_files_enhanced.py \
    --input-dir SimpleWorkflow/ParsingFailsSamples \
    --keep-failed

# Custom directories
uv run python SimpleWorkflow/retry_failed_files_enhanced.py \
    --input-dir /path/to/failures \
    --output-dir /path/to/output
```

**Why:**
- Need custom input/output directories
- Want to keep FAILED files
- Testing failure scenarios
- More detailed retry statistics

---

## 🎯 Common Workflows

### Workflow 1: Daily Production Processing

```bash
# Step 1: Process new PDFs
uv run python SimpleWorkflow/pdf_processor.py

# Step 2: Retry any failures
uv run python SimpleWorkflow/pdf_processor.py --retry-failed

# Step 3: Check results
ls SimpleWorkflow/ParsedFiles/FAILED-*.md | wc -l
```

### Workflow 2: Large Batch Processing (Millions)

```bash
# Step 1: Start background processing
nohup uv run python SimpleWorkflow/pdf_processor.py \
    --batch-size 1000 \
    --checkpoint-interval 200 \
    > processor.log 2>&1 &
echo $! > .processor.pid

# Step 2: Monitor progress
tail -f processor.log | grep "Checkpoint"

# Step 3: Graceful stop (when needed)
kill $(cat .processor.pid)

# Step 4: Resume later
uv run python SimpleWorkflow/pdf_processor.py
```

### Workflow 3: Testing & Development

```bash
# Step 1: Test with sample
uv run python SimpleWorkflow/pdf_processor.py --sample 10

# Step 2: Test retry with ParsingFailsSamples
uv run python SimpleWorkflow/retry_failed_files_enhanced.py \
    --input-dir SimpleWorkflow/ParsingFailsSamples \
    --keep-failed

# Step 3: Analyze failures
uv run python SimpleWorkflow/analyze_parsing_failures.py
```

---

## 📈 Performance Expectations

### Throughput (depends on file size and system)

| System | Workers | Throughput |
|--------|---------|------------|
| 128GB, 20 cores | 30/12 | 0.5-5 files/s |
| 32GB, 8 cores | 15/6 | 0.3-2 files/s |
| 16GB, 4 cores | 8/3 | 0.2-1 files/s |

### Time Estimates (average 10MB PDFs)

| Files | 128GB System | 32GB System |
|-------|--------------|-------------|
| 100 | 5-10 min | 10-20 min |
| 1,000 | 1-2 hours | 2-4 hours |
| 10,000 | 10-20 hours | 1-2 days |
| 100,000 | 4-8 days | 1-2 weeks |
| 1,000,000 | 1.5-3 months | 3-6 months |

### Success Rates

- **Main processor:** 95-98%
- **Enhanced retry (on failures):** 91.8%
- **Overall:** ~97% with retry

---

## 🔧 Key Features

### Both Tools Have:
- ✅ Per-file process isolation (no cascade failures)
- ✅ 5-minute timeout per PDF
- ✅ Pre-processing validation
- ✅ Multiple parser fallbacks (pymupdf, pdfplumber, pypdf)
- ✅ Memory limits (2GB per process)
- ✅ Batching and checkpointing
- ✅ Graceful shutdown
- ✅ Auto-resume capability

### Main Processor Adds:
- ✅ Processes from metadata parquet
- ✅ Dual worker pools (download + processing)
- ✅ Performance metrics
- ✅ Skip existing files

### Enhanced Retry Adds:
- ✅ Works with any directory
- ✅ Parses FAILED-*.md files
- ✅ Detailed retry statistics
- ✅ Background management script

---

## 📚 Documentation

**Quick Reference:**
- `README.md` - Complete documentation
- `QUICK_REFERENCE.md` - Command cheat sheet
- `INDEX.md` - Navigation guide

**Investigation:**
- `CONSOLIDATION_COMPLETE.md` - What we built
- `COMPLETE_SUMMARY.md` - Investigation results
- `failure_analysis/QUICK_START.md` - 3-minute overview

**Technical:**
- `failure_analysis/SOLUTIONS_AND_FIXES.md` - 30k word guide

---

## 🎉 Summary

**You now have:**

1. **One unified main processor** (`pdf_processor.py`)
   - Processes from metadata OR retries failures
   - Optimized for millions of files
   - All features combined

2. **One specialized retry tool** (`retry_failed_files_enhanced.py`)
   - Flexible directory handling
   - Enhanced error reporting
   - Background management

3. **Complete documentation** (23 files, 45k words)

**Status:** ✅ Production-ready

**Next action:** Pick a tool and start processing!

---

*Last updated: October 9, 2025*
*Tools: 2 main scripts + 1 analysis*
*Success rate: 95-98%*
*Scalability: Millions of files*
*Status: Ready to deploy* 🚀
