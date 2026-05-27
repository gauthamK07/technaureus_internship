principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time: "))

simple_interest = 0
simple_interest += (principal * rate * time) / 100

print("Simple Interest =", simple_interest)