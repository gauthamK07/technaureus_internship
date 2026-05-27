class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name :",self.name)
        print("Salary :",self.salary)
class manager(employee):
    def manage(self):
        print(self.name," is managing the team")

class developer(employee):
    def develop(self):
        print(self.name," is developing the code")

m1=manager("Gautham",50000)
d1=developer("John",60000)

m1.display()
m1.manage()
print()
d1.display()
d1.develop()
