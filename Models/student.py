from models.person import Person

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.__courses = []   # private variable

    def enroll_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)
        else:
            print("Course already enrolled")

    def get_courses(self):
        return self.__courses

    def display_details(self):
        super().display_details()
        print("Courses:", self.__courses)
