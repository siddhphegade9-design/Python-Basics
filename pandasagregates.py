import pandas as pd
#aggregate function = Reduces a set of values into a single summary value .
#Used to summarize and analyse data.
#Often used with the groupby() function.

df = pd.read_csv("data.csv")

print(df.mean(numeric_only= True))
