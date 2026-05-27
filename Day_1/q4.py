principal = int(input("Enter the principal amount: "))   
rate = float(input("Enter the annual interest rate (in %): "))          
time = int(input("Enter the time in years: "))         
amount = principal
for i in range(1, time + 1):
    amount *= (1 + rate / 100)
compound_interest = amount - principal
print("Final Amount =", amount)
print("Compound Interest =", compound_interest)