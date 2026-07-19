import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"D:\Data_Analytics_Project\Dataset\Sample.csv",
    encoding="cp1252"
)

subcategory_summary = (
    df.groupby("Sub-Category")
    [["Sales" , "Profit"]]
    .sum()
    .sort_values(by= "Sales" , ascending=False)
)

print("=" * 50)
print("Sub-Category Sales and Profit")
print("=" * 50)

print(subcategory_summary)