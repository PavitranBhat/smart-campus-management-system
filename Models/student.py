from models.person import Person

class Student(Person):
    def __init__(self, person_id, name, department, year):
        super().__init__(person_id, name)
        self.department = department
        self.year = year

    def display_info(self):  # Method overriding
        base_info = super().display_info()
        base_info.update({
            "role": "Student",
            "department": self.department,
            "year": self.year
        })
        return base_info
