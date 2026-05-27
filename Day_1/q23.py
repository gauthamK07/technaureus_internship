num = int(input("Enter a number: "))
bit = int(input("Enter bit position: "))

set_bit = num | (1 << bit)
clear_bit = num & ~(1 << bit)

print("After setting bit =", set_bit)
print("After clearing bit =", clear_bit)