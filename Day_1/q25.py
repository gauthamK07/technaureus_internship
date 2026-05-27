a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
mul=0
for i in range(1, b+1):
    mul+=a
print("The product of", a, "and", b, "is:", mul)
