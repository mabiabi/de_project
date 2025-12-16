import pandas as pd
import os

def convert_excel_to_csv(excel_path, output_path):
    print(f"Reading Excel file: {excel_path}")
    df = pd.read_excel(excel_path)  # requires openpyxl (already installed)
    
    print(f"Saving CSV file: {output_path}")
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    excel_file = "/workspaces/de_project_1/data/raw/Online Retail.xlsx"
    csv_file = "/workspaces/de_project_1/data/raw/online_retail.csv"

    convert_excel_to_csv(excel_file, csv_file)
    print("✔ Conversion complete.")