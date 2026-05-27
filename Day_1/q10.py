ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print("Uppercase letter")
elif 'a' <= ch <= 'z':
    print("Lowercase letter")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special character")