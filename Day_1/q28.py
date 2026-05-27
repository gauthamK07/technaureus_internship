m1=int(input("Enter mark of subjec 1:"))
m2=int(input("Enter mark of subject 2:"))
m3=int(input("Enter mark of subject 3:"))
m4=int(input("Enter mark of subject 4:"))
m5=int(input("Enter mark of subject 5:"))

total= m1+m2+m3+m4+m5
if total>=90:
    print("Grade A")
elif total>=80:
    print("Grade B")
elif total>=70:
    print("Grade C")
elif total>=60:
    print("Grade D")
else:
    print("Grade F")
percentage= (total/500)*100
print("Percentage:", percentage)