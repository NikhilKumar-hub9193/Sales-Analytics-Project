import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(
    r"D:\Data_Analytics_Project\Dataset\Sample.csv",
    encoding="cp1252"
)

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 60)
print("TOP 10 CUSTOMER BY SALES")
print("=" * 60)

plt.figure(figsize=(14,6))

bars = plt.bar(
    top_customers.index,
    top_customers.values
)

plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer Name")
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
plt.close