def retry_function():
    m=3
    while m>0:
        try:
            a=int(input("Enter integer:"))
            print("success")
        except ValueError:
            print("not an integer")
            m-=1
            if m>0:
                print(" retry")
            else:
                print("max retries exceeded")
retry_function()