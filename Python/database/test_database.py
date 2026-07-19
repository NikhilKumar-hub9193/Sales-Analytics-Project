import sqlite3
import pandas as pd

conn = sqlite3.connect(r"D:\Data_Analytics_Project\Database\sales_analysis.db")

query = """
SELECT COUNT(*) AS Total_Records
FROM superstore
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()