import pandas as pd
data = ["Python", "Java", "C++", "JavaScript", "Ruby"]
series = pd.Series(data, index=[1,2,3,4,5])
print(series)

print(series.loc[3]) #locates data at index 3
print(series.iloc[0]) #locates data at position 0

series.loc[6] = "Rust" #Can add new data at a newer index
series.loc[5] = "C" #Can also update exisiting one
print(series)


data1 = [100,102,104,200,202]
series1=pd.Series(data1,index=["a","b","c","d","e"])

print(series1[series1>=200]) #Filters data greater than or equal to 200

calories = {"day1": 420, "day2": 380, "day3": 390}
series2 = pd.Series(calories)

series2.loc["day2"] += 500  #Updates the value of day2 by adding 500 to it
print(series2)

print(series2[series2<500])
