import pandas as pd

df= pd.read_csv("data.csv")
print(df)

print(df.to_string()) #Displays entire Data

print(df["Name"]) #Gives the entire Name Column Data

print(df.loc[2]) #Gives the entire Data of Row at Index 2


df1 = pd.read_csv("data.csv", index_col="Name") #Dets the Name Column as Index Column
print(df1)

print(df.loc["Charizard",["Height","Weight"]]) #Gives only the Height and Weight of Charizard


#SELECTION BY COLUMN
#print(df["Name"].to_string())
#print(df["Height"].to_string())

#SELECTION BY ROWS
#print(df.iloc[0])
#print(df.loc["Charizard"])

