for i in range(1, 5 + 1):
        for j in range(5 - i):
            print(" ", end="")
        if i == 1:
            print("*")
        elif i == 5:
            for j in range(2 * 5 - 1):
                print("*", end="")
            print()
        else:
            print("*", end="")
            for j in range(2 * i - 3):
                print(" ", end="")
            print("*")