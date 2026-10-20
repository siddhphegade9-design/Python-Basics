#f = open("data.txt", "r") #You can also use "rt" instead of r.
#data = f.read()
#print(data)

string = "hello my name is dustin and i do python"

#f = open("data.txt", "w") #You can write to a file using "w" or "wt"
#data1 = f.write(string) #This doesnt print the new data but does save the new data in the file.
#f.close()
#print(data1) #This will print the number of characters written to the file


#f = open("data.txt", "a") #You can append to a file using "a" or "at"
#data2 = f.write(string) #This doesnt print the new data but does save the new data in the file.
#f.close()

f = open("data.txt", "r") 
for line in f:
    print(line) #This will print the data in the file line by line

f.close()

'''with open("data.txt", "r") as f: #This is a better way to open a file because it automatically closes the file after the block of code is executed.
    data = f.read()
    print(data)'''


