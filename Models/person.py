from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, id):
        self.name = name
        self._id = id

    @abstractmethod
    def display_details(self):
        pass
