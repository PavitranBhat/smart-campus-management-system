class Faculty:

    def __init__(self, name, faculty_id, subject):
        self.name = name
        self.faculty_id = faculty_id
        self.subject = subject

    def display_details(self):
        print("Faculty Name:", self.name)
        print("Faculty ID:", self.faculty_id)
        print("Subject:", self.subject)
