import pandas as pd
from pathlib import Path


def read_sales_csv(file_path: str, nrows: int | None = None) -> pd.DataFrame:
    """
    Extracts a sales CSV file from data/raw into a pandas DataFrame.

    Parameters
    ----------
    file_path : str
        Path to the raw CSV file.
    nrows : int | None
        Optional limit on number of rows to read (for debugging).

    Returns
    -------
    pd.DataFrame
        Loaded data.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path}")

    print(f"📥 Loading CSV: {path}")
    df = pd.read_csv(path, nrows=nrows)

    print(f"✔ Loaded {len(df):,} rows, {len(df.columns)} columns.")
    print("📊 Columns:", list(df.columns))

    return df
