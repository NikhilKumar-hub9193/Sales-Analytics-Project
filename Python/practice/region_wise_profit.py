import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"D:\Data_Analytics_Project\Dataset\Sample.csv",
    encoding="cp1252"
)

region_wise_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("=" * 50)
print("REGION-WISE PROFIT")
print("=" * 50)

bars = plt.bar(
    region_wise_profit.index,
    region_wise_profit.values
)

plt.title("Region-wise Profit")
plt.xlabel("Region")
plt.ylabel("Total Profit")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

print(region_wise_profit)
plt.tight_layout()
plt.show()
plt.close()

subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)