# SimpleWorkflow - PDF to Markdown Converter

A robust Python script that downloads PDFs from S3 and converts them to Markdown format for RAG (Retrieval-Augmented Generation) applications.

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

## 📁 File Structure

```
SimpleWorkflow/
├── README.md                           # This file
├── sql_metadata_to_parsed_markdown.py  # Main script
├── ParsedFiles/                        # Output directory
│   ├── {file_id}.md                   # Successfully processed files
│   └── FAILED-{file_id}.md            # Error reports for failed files
└── processing.log                      # Processing logs
```

## ⚙️ Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--max-files N` | Process only N files | `--max-files 100` |
| `--indices ID1 ID2...` | Process specific file IDs | `--indices "2129356319_ei-document_"` |
| `--sample N` | Process random sample of N files | `--sample 10` |
| `--skip-existing` | Skip already processed files (default) | `--skip-existing` |
| `--no-skip-existing` | Reprocess all files | `--no-skip-existing` |
| `--dry-run` | Preview what would be processed | `--dry-run` |

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

### Retry Failed Files

To retry only failed files:
1. Delete the `FAILED-*.md` files
2. Run the script again with `--skip-existing`

```bash
# Remove error reports
rm SimpleWorkflow/ParsedFiles/FAILED-*.md

# Retry processing
uv run python SimpleWorkflow/sql_metadata_to_parsed_markdown.py --skip-existing
```

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

- **Automatic Retry**: Failed S3 downloads retry up to 3 times
- **Error Recovery**: Failures don't stop the entire batch
- **Clean Temporary Files**: Automatically cleans up temp files
- **Skip System Files**: Ignores macOS system files (__MACOSX, ._ files)
- **Unicode Handling**: Safely handles problematic characters

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
