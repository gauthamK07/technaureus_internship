basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.80
gross_salary = basic_salary + hra + da

print("Gross Salary =", gross_salary)