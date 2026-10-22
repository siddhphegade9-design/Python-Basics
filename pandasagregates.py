import pandas as pd
#aggregate function = Reduces a set of values into a single summary value .
#Used to summarize and analyse data.
#Often used with the groupby() function.

df = pd.read_csv("data.csv")
#Whole Dataframe Aggregation

print(df.mean(numeric_only= True))#Gives the a mean values of numeric data only.
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))

print(df.count()) #counts the number of numeric datas.

#Single Columnn Aggregation
print(df["Height"].mean())
print(df["Height"].sum())