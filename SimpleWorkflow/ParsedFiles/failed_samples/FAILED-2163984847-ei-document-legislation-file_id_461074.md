---
file_identifier: 2163984847-ei-document-legislation-file_id_461074
status: FAILED
error: File is not a zip file
s3_key: sea-crawler/2163984847/ei-document/legislation/50/APENDICE-4.4.1-G_VELOCIDAD-Y-ALTURA-DE-ESCURRIMIENTO/G.-Velocidad-y-altura-de-escurrimiento/23067-HD-GENERAL-LAM-008.pdf
---

# Processing Failed

Traceback (most recent call last):
  File "/home/alejandro/Desktop/repos/NVIRO-airflow-parsing/SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py", line 358, in process_single_pdf_optimized
    _, pdf_bytes = _extract_pdf_from_zip_bytes(content, prefer_name)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/alejandro/Desktop/repos/NVIRO-airflow-parsing/SimpleWorkflow/sql_metadata_to_parsed_markdown_optimized.py", line 203, in _extract_pdf_from_zip_bytes
    with zipfile.ZipFile(BytesIO(zip_bytes), "r") as zf:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/alejandro/.local/share/uv/python/cpython-3.12.4-linux-x86_64-gnu/lib/python3.12/zipfile/__init__.py", line 1349, in __init__
    self._RealGetContents()
  File "/home/alejandro/.local/share/uv/python/cpython-3.12.4-linux-x86_64-gnu/lib/python3.12/zipfile/__init__.py", line 1416, in _RealGetContents
    raise BadZipFile("File is not a zip file")
zipfile.BadZipFile: File is not a zip file

