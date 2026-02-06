from models.person import Person

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def display_details(self):
        super().display_details()
        print("Courses:", self.courses)
