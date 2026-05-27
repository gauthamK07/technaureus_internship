class Student:

    def __init__(self, name):

        self.name = name


class Teacher:

    def __init__(self, name):

        self.name = name


class Subject:

    def __init__(self, subject_name, teacher):

        self.subject_name = subject_name
        self.teacher = teacher


class Attendance:

    def __init__(self):

        self.records = {}

    def mark_attendance(self, student, status):

        self.records[student.name] = status

    def show_attendance(self):

        for student, status in self.records.items():

            print(student, ":", status)


t1 = Teacher("Anil Sir")

subject = Subject("Physics", t1)

s1 = Student("Rahul")

s2 = Student("Anu")

attendance = Attendance()

attendance.mark_attendance(s1, "Present")

attendance.mark_attendance(s2, "Absent")

print("Subject:", subject.subject_name)

print("Teacher:", subject.teacher.name)

attendance.show_attendance()