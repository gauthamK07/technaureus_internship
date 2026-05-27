a=int(input("Enter dividend: "))
b=int(input("Enter divisor: "))
quotient=0
temp=a
while temp>=b:
    temp-=b
    quotient+=1
print("Quotient =", quotient)