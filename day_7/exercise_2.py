class Student:
    def __init__(self, name, grades=None):
        self.name = name
        if grades is None:
            self.grades = []
        else:
            self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


student1 = Student("Tyler Durden")
student1.add_grade(90)
student1.add_grade(80)
student1.add_grade(70)

print(student1.average_grade())

student2 = Student("Richard Hendricks")
print(student2.average_grade())