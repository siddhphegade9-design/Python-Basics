def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper 
    return decorator

@repeat(5)
def say(a):
    print(f"hello {a}")

say("Siddh")
