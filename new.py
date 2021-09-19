Name = "Sham"
Grades = (34, 54, 45, 56)

class Student:
    def __init__(self):
        self.name = Name
        self.grades = Grades
    def average_grade(self):
        avg = sum(Grades) / len(Grades)
        print("{} has an avg grade of {}%".format(Name, avg))

student = Student()
student.average_grade()