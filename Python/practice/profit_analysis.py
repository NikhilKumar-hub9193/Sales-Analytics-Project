import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"D:\Data_Analytics_Project\Dataset\Sample.csv",
    encoding="cp1252"
)

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("=" * 50)
print("CATEGORY-WISE PROFIT")
print("=" * 50)
print(category_profit)

plt.figure(figsize=(8,5))

bars = plt.bar(
    category_profit.index,
    category_profit.values
)

plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Category Profit")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()
plt.show()