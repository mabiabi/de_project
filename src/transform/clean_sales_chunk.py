import pandas as pd


def clean_sales_chunk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans a single chunk of sales data (Silver layer).
    """

    # 1. Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    # we are standardizing column names by stripping whitespace, converting to lowercase, and replacing spaces with underscores.
    # When chains get long, they become hard to read. we can wrap the whole expression in parentheses to break it into multiple lines.

    # 2. Drop missing customer_id
    df = df.dropna(subset=["customerid"])
    # 

    # 3. Filter invalid business rows
    df = df[df["quantity"] > 0]
    df = df[df["unitprice"] > 0]

    # 4. Type casting
    df["customerid"] = df["customerid"].astype(int)
    df["invoicedate"] = pd.to_datetime(df["invoicedate"])

    # 5. Derived metric
    df["total_price"] = df["quantity"] * df["unitprice"]

    return df
