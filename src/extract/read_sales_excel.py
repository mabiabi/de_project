import pandas as pd

def read_sales_excel(path: str, nrows: int = None):
    df = pd.read_excel(path, nrows=nrows)
    return df