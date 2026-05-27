num = input("Enter a number: ")

is_binary = True

for digit in num:
    if digit != '0' and digit != '1':
        is_binary = False
        break

if is_binary:
    print("Binary number")
else:
    print("Not a binary number")