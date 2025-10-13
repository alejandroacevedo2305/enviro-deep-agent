"""
uv run python sql/labeled_docs_parsed.py
"""

import pandas as pd

df = pd.read_parquet("sql/metadata_table/flora_fauna_metadata_indexed.parquet")

if __name__ == "__main__":
    metadata_with_classes = "\n\n".join(
        [str(s) for s in df.metadata_with_classes.tolist()[0:2]]
    )
    print(metadata_with_classes)
