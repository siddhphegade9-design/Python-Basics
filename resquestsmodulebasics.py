import requests
#Suggest there website documents for info about packages and libraries of python.
r=requests.get('https://api.github.com/events')
#what this does is reads the data from the url and stores it in the variable r. The data is in JSON format, 
# which is a common format for APIs to return data. You can access the data using r.json() to get a Python dictionary or list,
# depending on the structure of the JSON data returned by the API.
print(r.text)

#with open("github_events.json", "w") as f:
#    f.write(r.text)
#what this does is it opens a file called "github_events.json" in write mode and writes the text content of the response (r.text) to that file.

