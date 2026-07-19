import pandas as pd
import sqlite3
from pathlib import Path

# Project path
project_path = Path(r"D:\Data_Analytics_Project")

# CSV file path
csv_path = project_path / "Dataset" / "Sample.csv"

# Read CSV
df = pd.read_csv(csv_path, encoding="cp1252")

# Clean text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("\xa0", " ", regex=False)
        .str.replace("“", '"')
        .str.replace("”", '"')
        .str.replace("’", "'")
    )

# Create Database folder
db_folder = project_path / "Database"
db_folder.mkdir(exist_ok=True)

# Database path
db_path = db_folder / "sales_analysis.db"

# Create SQLite database
conn = sqlite3.connect(db_path)

# Save table
df.to_sql("superstore", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")
print("Database Path:", db_path)