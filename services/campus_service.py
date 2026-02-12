from models.student import Student
from models.faculty import Faculty
from models.course import Course


class CampusService:
    def __init__(self):
        self.students = {}
        self.faculties = {}
        self.courses = {}

    # --------------------------
    # STUDENT OPERATIONS
    # --------------------------

    def add_student(self, student_id, name, department, year):
        if student_id in self.students:
            return None

        student = Student(student_id, name, department, year)
        self.students[student_id] = student
        return student

    def get_student(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        return [s.display_info() for s in self.students.values()]

    def update_student(self, student_id, data):
        student = self.students.get(student_id)
        if not student:
            return None

        if "department" in data:
            student.department = data["department"]
        if "year" in data:
            student.year = data["year"]

        return student

    def delete_student(self, student_id):
        return self.students.pop(student_id, None)

    # --------------------------
    # FACULTY OPERATIONS
    # --------------------------

    def add_faculty(self, faculty_id, name, specialization):
        if faculty_id in self.faculties:
            return None

        faculty = Faculty(faculty_id, name, specialization)
        self.faculties[faculty_id] = faculty
        return faculty

    def get_all_faculties(self):
        return [f.display_info() for f in self.faculties.values()]

    # --------------------------
    # COURSE OPERATIONS
    # --------------------------

    def add_course(self, course_id, title):
        if course_id in self.courses:
            return None

        course = Course(course_id, title)
        self.courses[course_id] = course
        return course

    def enroll_student_to_course(self, course_id, student_id):
        course = self.courses.get(course_id)
        student = self.students.get(student_id)

        if not course or not student:
            return None

        course.enroll_student(student)
        return course
