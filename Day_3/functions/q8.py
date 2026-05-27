def validator(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg,int):
                print("All values must be integers")
                return 
        return func(*args)
    return wrapper



    

@validator
def add(a,b):
    return a+b

print("Result",add(99,22))
print("Result",add(1,"hello"))


