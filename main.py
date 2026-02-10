from models.student import Student
from models.faculty import Faculty

s1 = Student("Pavitra", "S101")
s1.enroll_course("Python")

f1 = Faculty("Dr Rao", "F201", "Data Science")

people = [s1, f1]

for person in people:
    print("------------")
    person.display_details()
