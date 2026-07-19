import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"D:\Data_Analytics_Project\Dataset\Sample.csv",
    encoding="cp1252"
)

subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 60)
print("TOP 10 SUB-CATEGORIES BY SALES")
print("=" * 60)

print(subcategory_sales)

plt.figure(figsize=(12,6))

bars = plt.bar(
    subcategory_sales.index,
    subcategory_sales.values
)

plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=45, ha="right")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=8
    )

plt.tight_layout()
plt.show()
