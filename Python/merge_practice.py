import pandas as pd
sales = pd.DataFrame({
    "Emp_ID" : [101, 102, 103],
    "Name" : ["Nikhil" , "Yash" , "Manish"],
    "Sales" : [50000 , 75000 , 84000]
})

department = pd.DataFrame({
    "Emp_ID": [101, 102, 103],
    "Department": ["Sales", "Marketing", "HR"]
})

'''
# Inner Join
merged_data = pd.merge(
    sales,
    department,
    on="Emp_ID"
)
'''

# Left Join
merged_data = pd.merge(
    sales,
    department,
    on="Emp_ID",
    how="left"
)

print(merged_data)