def marks(**kwargs):
    #kwargs is a dictonary with all the key value pairs which were passed to marks.
    for item in kwargs.items():
        print(item)


marks(John=90, Mike=80, Sarah=95, Tom=85) #This will print the key value pairs in the dictonary.



def function(*args,**kwargs):
    print(args) #This will print the tuple of all the positional arguments passed to the function.
    print(kwargs) #This will print the dictonary of all the keyword arguments passed to the function.


function(1,2,3,4,5,John=90, Mike=80, Sarah=95, Tom=85)