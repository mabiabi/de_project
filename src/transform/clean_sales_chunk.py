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



    # 3. Filter invalid business rows
    df = df[df["quantity"] > 0]
    # df["quantity"] > 0
    # Accesses the "quantity" column
    # Creates a boolean mask (Series of True/False values)
    # Each row gets True if quantity > 0, False otherwise
    
    # df[boolean_mask]
    # Uses the boolean mask to filter rows
    # Keeps only rows where mask is True

    # df = ...
    # Reassigns the filtered DataFrame back to df
    # Original df is replaced (this is in-place filtering)

    df = df[df["unitprice"] > 0]
    





    # 4. Type casting
    df["customerid"] = df["customerid"].astype(int)
    df["invoicedate"] = pd.to_datetime(df["invoicedate"])

    # 5. Derived metric
    df["total_price"] = df["quantity"] * df["unitprice"]

    return df
