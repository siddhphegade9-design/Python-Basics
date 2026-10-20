import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
}
df = pd.DataFrame(data, index=["Employee1", "Employee2", "Employee3", "Employee4"])
print(df)

print(df.loc["Employee2"])  # Accessing data using loc function

#Adding a new Column to the DataFrame
df["Department"] = ["HR", "Finance", "IT", "Marketing"]
print(df)

#Adding a new Row to the DataFrame
new_row = pd.DataFrame({"Name": ["Eve"], "Age": [28], "Department": ["Sales"]}, index=["Employee5"])
df = pd.concat([df, new_row])
print(df)
