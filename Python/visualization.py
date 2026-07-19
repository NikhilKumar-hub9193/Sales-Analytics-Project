import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(
    r"D:\Data_Analytics_Project\Dataset\Sample.csv",
    encoding="cp1252"
)

'''
# Bar Chart

# Category-wise Sales
category_wise = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Create Figure
plt.figure(figsize=(8, 5))

# Bar Chart
bars = plt.bar(category_wise.index, category_wise.values)

# Title and Labels
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

# Add Data Labels
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
plt.close()
'''

'''
# Bar Chart

# Region - Wise Sales
region_wise = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Create Figure
plt.figure(figsize=(8, 5))

# Bar Chart
bars = plt.bar(region_wise.index , region_wise.values)

# Title and Lables
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")

# Add Data Lables
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
plt.close()
'''

# Pie Chart
'''
# Category-wise Sales
category_wise = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Create Figure
plt.figure(figsize=(7,7))

# Pie Chart
plt.pie(
    category_wise.values,
    labels=category_wise.index,
    autopct="%1.1f%%",
    startangle=90
)

# Title
plt.title("Category-wise Sales Distribution")

plt.show()
plt.close()

'''

# Line Chart

# Convert Order Date into Date format
df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

print(monthly_sales)

plt.figure(figsize=(10,5))

plt.plot(
    monthly_sales["Month"].astype(str),
    monthly_sales["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()