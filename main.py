from Models.student import Student
from Models.Faculty import Faculty

# Create student
s1 = Student("Pavitra", "S101")
s1.enroll_course("Python")
s1.display_details()

# Create faculty
f1 = Faculty("Dr. Rao", "F201", "Data Science")
f1.display_details()
