class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.students = []   # Composition (HAS-A relationship)

    def enroll_student(self, student):
        self.students.append(student)

    def get_course_info(self):
        return {
            "course_id": self.course_id,
            "title": self.title,
            "students": [s.get_name() for s in self.students]
        }
