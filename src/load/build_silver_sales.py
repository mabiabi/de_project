from src.extract.read_sales_csv_chunked import read_sales_csv_in_chunks
from src.transform.clean_sales_chunk import clean_sales_chunk
from pathlib import Path

OUTPUT_PATH = Path("data/processed/sales_silver.csv")

def build_silver_layer():
    first_write = True

    for chunk in read_sales_csv_in_chunks(
        "data/raw/online_retail.csv",
        chunk_size=100_000
    ):
        cleaned = clean_sales_chunk(chunk)

        cleaned.to_csv(
            OUTPUT_PATH,
            mode="w" if first_write else "a",
            header=first_write,
            index=False
        )

        first_write = False

        print(f"Written {len(cleaned):,} rows to silver layer")
        

if __name__ == "__main__": # what???
    build_silver_layer()