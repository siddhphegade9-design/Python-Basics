import pandas as pd

df = pd.read_csv("data.csv")
print(df)

print(df.to_string())  # Displays entire data

print(df["Name"])  # Entire Name column

print(df.loc[2])  # Entire row at index 2

df1 = pd.read_csv("data.csv", index_col="Name")  # Name column as index
print(df1)

print(df1.loc["Charizard", ["Height", "Weight"]])  # Height and Weight of Charizard (uses df1!)

# SELECTION BY COLUMN
# print(df["Name"].to_string())
# print(df["Height"].to_string())

# SELECTION BY ROWS
# print(df.iloc[0])
# print(df1.loc["Charizard"])  # needs df1 too
# print(df.iloc[0:10:2])

tall_pokemon = df[df["Height"] >= 2]
print(tall_pokemon)

legendary_pokemon = df[df["Legendary"] == True]
print(legendary_pokemon)

ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(ff_pokemon)