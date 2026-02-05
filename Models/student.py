class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def display_details(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Courses:", self.courses)

    def enroll_course(self, course):
        self.courses.append(course)
