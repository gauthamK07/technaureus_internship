a=int(input("Enter length of side 1 :"))
b=int(input("Enter length of side 2 :"))
c=int(input("Enter length of side 3 :"))

if a+b>c and a+c>b and b+c>a:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")