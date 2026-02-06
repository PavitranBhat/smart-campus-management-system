from models.student import Student
from models.faculty import Faculty

s1 = Student("Pavitra", "S101")
s1.enroll_course("Python")
s1.display_details()

print("-------------")

f1 = Faculty("Dr Rao", "F201", "Data Science")
f1.display_details()
