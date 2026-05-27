a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
remainder = a - (a // b) * b
print("Remainder =", remainder)