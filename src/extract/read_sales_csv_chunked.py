import pandas as pd
from pathlib import Path
from typing import Iterator


def read_sales_csv_in_chunks(
    file_path: str,
    chunk_size: int = 100_000
) -> Iterator[pd.DataFrame]:
    """
    Generator that yields chunks of a large CSV file.

    This simulates Spark-style partitioned reading.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path}")

    print(f"📥 Reading CSV in chunks of {chunk_size:,} rows")

    for i, chunk in enumerate(pd.read_csv(path, chunksize=chunk_size)):
        print(f"➡ Chunk {i + 1} loaded ({len(chunk):,} rows)")
        yield chunk
