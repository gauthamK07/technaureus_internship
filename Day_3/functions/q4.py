def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def calculator(funct,a,b):
    return funct(a,b)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Sum: ",calculator(add,a,b))
print("Difference: ",calculator(sub,a,b))
print("Product: ",calculator(mul,a,b))
print("Division: ",calculator(div,a,b))