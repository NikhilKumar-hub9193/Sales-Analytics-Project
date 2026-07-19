import pandas as pd
 
df = pd.read_csv(
    r"D:\Data_Analytics_Project\Dataset\Sample.csv",
    encoding="cp1252"
)

'''
pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum"
)

'''

pivot = pd.pivot_table(
    df,
    values=["Sales", "Profit"],
    index="Region",
    columns="Category",
    aggfunc="sum"
)
print(pivot)