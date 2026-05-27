num = int(input("Enter a number: "))
bit = int(input("Enter bit position to toggle: "))

result = num ^ (1 << bit)

print("Result =", result)