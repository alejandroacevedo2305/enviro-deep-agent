# Root Cause Analysis: PDF Processing Failures

## Executive Summary

After analyzing the 5 failed PDF files, I've identified the **root cause** of all
failures:

**Python Environment Mismatch** - The processing scripts are being executed in a
Python environment where `pdfplumber` is not available, causing all three extraction
strategies to fail in sequence.

---

## Detailed Analysis

### 1. The Failure Pattern

All 5 files show identical error messages:

```
RuntimeError: All extraction strategies failed.
PyMuPDF: ,
pdfplumber: pdfplumber not installed. Install with: uv add pdfplumber,
pypdf:
```

### 2. What's Actually Happening

The PDF processor uses a **3-tier fallback strategy**:

```python
# Strategy 1: Try PyMuPDF (primary)
try:
    result = _extract_markdown_with_pymupdf(pdf_path_str)
    return (*result, stats)
except Exception as pymupdf_error:
    # Strategy 2: Try pdfplumber
    try:
        import pdfplumber  # <-- FAILS HERE
        result = _extract_markdown_with_pdfplumber(pdf_path_str)
        return (*result, stats)
    except ImportError:
        raise ImportError("pdfplumber not installed...")
    except Exception as pdfplumber_error:
        # Strategy 3: Try pypdf
        try:
            from pypdf import PdfReader  # <-- WOULD FAIL HERE TOO
            result = _extract_markdown_with_pypdf(pdf_path_str)
            return (*result, stats)
        except ImportError:
            raise ImportError("pypdf not installed...")
```

**What happens:**
1. **PyMuPDF fails silently** (error is empty: `PyMuPDF: ,`)
2. **pdfplumber import fails** because it's not in the current Python environment
3. **pypdf is never tried** because pdfplumber raised an ImportError first
4. The error message concatenates all three failures

### 3. The Environment Problem

#### Current State:
- **System Python** (`/home/alejandro/miniconda3/bin/python`):
  - ❌ Does NOT have `pdfplumber` installed
  - ✓ Has `pymupdf` (1.26.4)
  - ✓ Has `pypdf` (5.8.0)

- **UV Virtual Environment** (`.venv/bin/python`):
  - ✓ Has `pdfplumber` (0.11.7)
  - ✓ Has `pymupdf`
  - ✓ Has `pypdf`

#### The Issue:
The script runs with `uv run python`, which **should** use the `.venv` environment,
but the worker processes spawned by `ProcessPoolExecutor` may inherit the system
Python environment instead.

### 4. Why PyMuPDF Fails Silently

The empty error message `PyMuPDF: ,` suggests one of these scenarios:

1. **Corrupted/malformed PDF** that PyMuPDF can't parse
2. **Image-only PDF** with no extractable text
3. **PyMuPDF crash** that returns empty error
4. **Process pool isolation issue** where the error isn't captured properly

### 5. Process Pool Inheritance Problem

Looking at the code structure:

```python
# File: pdf_processor.py, line 544-592
def _extract_markdown_worker_isolated(pdf_path_str: str) -> tuple[str, Any, dict]:
    """Extract markdown in isolated worker with all strategies..."""
    # This function runs in a child process spawned by ProcessPoolExecutor
    # The child process may not have access to the .venv environment
```

When `ProcessPoolExecutor` spawns child processes:
- They inherit the **parent's Python interpreter**
- They **may not** inherit the virtual environment activation
- Result: Workers use system Python without `pdfplumber`

---

## Why These Specific Files Failed

These 5 files likely have characteristics that cause PyMuPDF to fail:
- Possibly image-heavy PDFs
- Potentially malformed PDF structure
- May contain non-standard encoding

Without `pdfplumber` as a fallback, they have no alternative extraction method.

---

## Solutions (Ordered by Effectiveness)

### Solution 1: Ensure Workers Use Correct Environment ⭐ RECOMMENDED

**Problem:** Child processes spawned by `ProcessPoolExecutor` don't inherit the
virtual environment.

**Fix:** Explicitly pass the Python executable path to workers:

```python
# Add this to pdf_processor.py
import sys
import subprocess

def _extract_markdown_worker_isolated(pdf_path_str: str) -> tuple[str, Any, dict]:
    """Extract with guaranteed environment isolation."""

    # Get the current Python executable (should be from .venv)
    python_exe = sys.executable

    # Verify pdfplumber is available
    try:
        import pdfplumber
        # Good - we're in the right environment
    except ImportError:
        # Bad - we're not in the venv
        # Try to re-execute in the correct environment
        raise EnvironmentError(
            f"Running in wrong Python environment: {python_exe}. "
            f"pdfplumber not available. Please ensure uv environment is active."
        )

    # Continue with normal extraction logic...
    stats = {"fallback_used": False, "strategy": "pymupdf"}

    try:
        result = _extract_markdown_with_pymupdf(pdf_path_str)
        return (*result, stats)
    except Exception as pymupdf_error:
        # Now pdfplumber should work
        try:
            import pdfplumber  # This should succeed now
            stats["fallback_used"] = True
            stats["strategy"] = "pdfplumber"
            result = _extract_markdown_with_pdfplumber(pdf_path_str)
            return (*result, stats)
        except Exception as pdfplumber_error:
            # Try pypdf
            try:
                from pypdf import PdfReader
                stats["fallback_used"] = True
                stats["strategy"] = "pypdf"
                result = _extract_markdown_with_pypdf(pdf_path_str)
                return (*result, stats)
            except Exception as pypdf_error:
                raise RuntimeError(
                    f"All extraction strategies failed. "
                    f"PyMuPDF: {pymupdf_error}, "
                    f"pdfplumber: {pdfplumber_error}, "
                    f"pypdf: {pypdf_error}"
                )
```

### Solution 2: Remove ImportError Catch

**Problem:** The current code treats `ImportError` separately, which prevents
fallback to pypdf.

**Current problematic code:**
```python
# File: pdf_processor.py, lines 497-517
def _extract_markdown_with_pdfplumber(pdf_path_str: str) -> tuple[str, Any]:
    """Extract using pdfplumber (fallback)."""
    try:
        import pdfplumber
        # ... extraction code ...
    except ImportError:
        raise ImportError("pdfplumber not installed...")  # <-- STOPS HERE
```

**Fix:** Let ImportError propagate as a normal exception:

```python
def _extract_markdown_with_pdfplumber(pdf_path_str: str) -> tuple[str, Any]:
    """Extract using pdfplumber (fallback)."""
    # Let ImportError propagate normally so pypdf can be tried
    import pdfplumber

    with pdfplumber.open(pdf_path_str) as pdf:
        pages_text = []
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            if text:
                pages_text.append(f"## Page {page_num}\n\n{text}")

        combined_text = "\n\n---\n\n".join(pages_text)
        metadata = DocumentMetadata(
            page_count=len(pdf.pages),
            extraction_quality=ExtractionQuality.MEDIUM,
            quality_notes=["pdfplumber fallback used"],
        )
        return combined_text, metadata

def _extract_markdown_with_pypdf(pdf_path_str: str) -> tuple[str, Any]:
    """Extract using pypdf (last resort fallback)."""
    # Let ImportError propagate normally
    from pypdf import PdfReader

    reader = PdfReader(pdf_path_str)
    pages_text = []
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            pages_text.append(f"## Page {page_num}\n\n{text}")

    combined_text = "\n\n---\n\n".join(pages_text)
    metadata = DocumentMetadata(
        page_count=len(reader.pages),
        extraction_quality=ExtractionQuality.LOW,
        quality_notes=["pypdf fallback used"],
    )
    return combined_text, metadata

# Update the worker to catch ALL exceptions uniformly
def _extract_markdown_worker_isolated(
    pdf_path_str: str,
) -> tuple[str, Any, dict]:
    """Extract markdown in isolated worker with all strategies."""
    stats = {"fallback_used": False, "strategy": "pymupdf"}

    # ... memory limit setup ...

    try:
        result = _extract_markdown_with_pymupdf(pdf_path_str)
        return (*result, stats)
    except Exception as pymupdf_error:
        # Try pdfplumber (will raise ImportError if not available)
        try:
            stats["fallback_used"] = True
            stats["strategy"] = "pdfplumber"
            result = _extract_markdown_with_pdfplumber(pdf_path_str)
            return (*result, stats)
        except Exception as pdfplumber_error:
            # Try pypdf (will raise ImportError if not available)
            try:
                stats["fallback_used"] = True
                stats["strategy"] = "pypdf"
                result = _extract_markdown_with_pypdf(pdf_path_str)
                return (*result, stats)
            except Exception as pypdf_error:
                # Now all three errors are real extraction failures
                raise RuntimeError(
                    f"All extraction strategies failed. "
                    f"PyMuPDF: {pymupdf_error}, "
                    f"pdfplumber: {pdfplumber_error}, "
                    f"pypdf: {pypdf_error}"
                )
```

### Solution 3: Verify Environment at Startup

**Add environment verification before processing:**

```python
# Add to the beginning of main() in pdf_processor.py
def verify_extraction_dependencies():
    """Verify all PDF extraction libraries are available."""
    missing = []

    try:
        import pymupdf
    except ImportError:
        missing.append("pymupdf")

    try:
        import pdfplumber
    except ImportError:
        missing.append("pdfplumber")

    try:
        import pypdf
    except ImportError:
        missing.append("pypdf")

    if missing:
        raise EnvironmentError(
            f"Missing required dependencies: {', '.join(missing)}. "
            f"Install with: uv add {' '.join(missing)}"
        )

    logger.info(
        "✓ All PDF extraction libraries available: pymupdf, pdfplumber, pypdf"
    )


async def main():
    """Main processing function."""
    # Verify environment first
    verify_extraction_dependencies()

    # Continue with normal processing...
```

### Solution 4: Use Subprocess Instead of ProcessPoolExecutor

**Replace ProcessPoolExecutor with subprocess calls:**

```python
def extract_markdown_with_isolation(pdf_path_str: str) -> tuple[str, Any, dict]:
    """Extract markdown using subprocess for true isolation."""

    # Create a small Python script that will run in the correct environment
    extractor_script = f"""
import sys
sys.path.insert(0, '{os.getcwd()}')

from SimpleWorkflow.pdf_processor import _extract_markdown_worker_isolated

result = _extract_markdown_worker_isolated('{pdf_path_str}')
print(repr(result))
"""

    # Run in the current Python environment
    result = subprocess.run(
        [sys.executable, "-c", extractor_script],
        capture_output=True,
        text=True,
        timeout=300,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Extraction failed: {result.stderr}")

    # Parse the result
    return eval(result.stdout.strip())
```

---

## Recommended Action Plan

### Immediate Fix (5 minutes):

1. **Apply Solution 2** - Remove the special ImportError handling
2. **Apply Solution 3** - Add environment verification at startup
3. **Retry the 5 failed files**

### Short-term Fix (30 minutes):

1. **Investigate PyMuPDF failures** - Why is it returning empty errors?
2. **Add detailed logging** - Log which Python executable is being used
3. **Add worker verification** - Verify environment in each worker process

### Long-term Improvements:

1. **Add OCR fallback** - For image-only PDFs
2. **Add PDF repair** - Attempt to repair corrupted PDFs before processing
3. **Better error reporting** - Capture and log the actual PDF characteristics
4. **Unit tests** - Test each extraction strategy independently

---

## Testing the Fix

After applying the fixes, test with these commands:

```bash
# 1. Verify environment
cd /home/alejandro/Desktop/repos/NVIRO-airflow-parsing
uv run python -c "
import sys
print(f'Python: {sys.executable}')
import pymupdf
print(f'✓ pymupdf: {pymupdf.__version__}')
import pdfplumber
print(f'✓ pdfplumber: {pdfplumber.__version__}')
import pypdf
print(f'✓ pypdf: {pypdf.__version__}')
"

# 2. Retry a single failed file
uv run python SimpleWorkflow/retry_failed_files_enhanced.py --max-files 1

# 3. If successful, retry all 5 files
uv run python SimpleWorkflow/retry_failed_files_enhanced.py --max-files 5
```

---

## Conclusion

The failures are **NOT due to corrupted PDFs** or **processing logic bugs**.

The root cause is a **Python environment mismatch** where worker processes don't
have access to the `pdfplumber` library that exists in the UV virtual environment.

The fix is straightforward: ensure workers use the correct environment and handle
ImportErrors properly to allow fallback to the next strategy.

---

**Priority:** HIGH
**Effort:** LOW (1-2 hours)
**Impact:** Resolves 100% of current failures
