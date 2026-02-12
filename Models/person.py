class Person:
    def __init__(self, person_id, name):
        self._id = person_id      # Encapsulation
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def display_info(self):
        return {
            "id": self._id,
            "name": self._name
        }
