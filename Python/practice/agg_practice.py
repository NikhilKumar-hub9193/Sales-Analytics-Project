import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"D:\Data_Analytics_Project\Dataset\Sample.csv",
    encoding="cp1252"
)

'''
category_analysis = (
    df.groupby("Category")
    .agg({
        "Sales": ["sum", "mean"]
    })
)
'''

# Change Column Name
category_analysis = (
    df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Average_Sales=("Sales", "mean")
    )
)


print(category_analysis)