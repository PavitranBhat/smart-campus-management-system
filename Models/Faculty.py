from models.person import Person

class Faculty(Person):
    def __init__(self, name, faculty_id, subject):
        super().__init__(name, faculty_id)
        self.subject = subject

    def display_details(self):
        super().display_details()
        print("Subject:", self.subject)
