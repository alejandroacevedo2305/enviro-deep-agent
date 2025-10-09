"""
uv run python sql/labeled_docs_parsed.py
"""

import pandas as pd

df = pd.read_parquet("sql/metadata_table/flora_fauna_metadata_indexed.parquet")

if __name__ == "__main__":
    print(df["metadata"].iloc[0]["fileClass"])
