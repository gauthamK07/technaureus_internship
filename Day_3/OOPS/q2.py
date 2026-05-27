class student:
    def __init__(self):
        self.__marks=0
    def setMarks(self,marks):
        if marks < 0 and marks > 100:
            print("invalid")
        else:
            self.__marks=marks
    def getMarks(self):
        return self.__marks

stud=student()
stud.setMarks(100)
print(stud.getMarks())