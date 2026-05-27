a=int(input("Enter first number: "))
r=0
while a>0:
    r+=a%10
    a=a//10
if r==a :
    print("The number is amstrong.")
else:
    print("The number is not amstrong.")