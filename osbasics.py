import os

a = os.listdir("directory")
print(a)
print(os.getcwd()) #This will print the current working directory.
print(os.path.exists("sample.txt")) #This will check if the file exists in the current working directory.
#print(os.remove("sample.txt")) #This will remove the file from the current working directory.