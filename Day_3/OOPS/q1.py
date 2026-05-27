#multiple inheritance

class father:
    def skill1(self):
        print("Singing")

class mother:
    def skill2(self):
        print("Dancing")

class son(father,mother):
    def skill3(self):
        print("Acrobatics")

child=son()
child.skill1()
child.skill2()
child.skill3()
print(son.mro())
