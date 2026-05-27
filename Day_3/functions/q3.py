import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)
        end=time.time()
        print(f"Time taken to execute: {end-start}")
    return wrapper

@timer    
def factorial():
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))