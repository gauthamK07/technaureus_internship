def memoize(func):
    cache={}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args]=result
        return result
    return wrapper
@memoize
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
