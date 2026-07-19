import pandas as pd

# Load Dataset
df = pd.read_csv(
    r"D:\Data_Analytics_Project\Dataset\Sample.csv",
    encoding="latin1"
)

print("=" * 60)
print("        EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)

# 1. Shape
print("\n1. Dataset Shape")
print(df.shape)

# 2. Rows and Columns
print("\n2. Rows and Columns")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# 3. First 5 Records
print("\n3. First 5 Records")
print(df.head())

# 4. Last 5 Records
print("\n4. Last 5 Records")
print(df.tail())

# 5. Column Names
print("\n5. Column Names")
print(df.columns.tolist())

# 6. Data Types
print("\n6. Data Types")
print(df.dtypes)

# 7. Missing Values
print("\n7. Missing Values")
print(df.isnull().sum())

# 8. Duplicate Records
print("\n8. Duplicate Records")
print(df.duplicated().sum())

# 9. Statistical Summary
print("\n9. Statistical Summary")
print(df.describe())

print("\nEDA Completed Successfully!")