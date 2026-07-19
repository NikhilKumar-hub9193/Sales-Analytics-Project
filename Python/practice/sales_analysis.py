import pandas as pd

# Load Dataset
df = pd.read_csv(
    r"D:\Data_Analytics_Project\Dataset\Sample.csv",
    encoding="cp1252"
)

# Top 10 Products by Sales
'''
top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("=" * 60)
print("TOP 10 PRODUCTS BY SALES")
print("=" * 60)

print(top_products)
'''

# Top 10 Customer by Sales
'''
top_products = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 60)
print("TOP 10 CUSTOMER NAME BY SALES")
print("=" * 60)

print(top_products.reset_index())
'''

# Category wise Sales
'''
category_wise = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

print("=" * 60)
print(" CATEGORY - WISE TOTAL SALES")
print("=" * 60)

category_wise.rename(columns={"Sales" : "Total Sales"} , inplace=True)
print(category_wise)
'''
# Region - Wise Sales
'''
region_wise_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

print("=" * 60)
print(" REGION - WISE TOTAL SALES")
print("=" * 60)

region_wise_sales.rename(columns={"Sales" : "Total Sales"}, inplace=True)
print(region_wise_sales)
'''