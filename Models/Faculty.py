from models.person import Person

class Faculty(Person):
    def __init__(self, person_id, name, specialization):
        super().__init__(person_id, name)
        self.specialization = specialization

    def display_info(self):
        base_info = super().display_info()
        base_info.update({
            "role": "Faculty",
            "specialization": self.specialization
        })
        return base_info
