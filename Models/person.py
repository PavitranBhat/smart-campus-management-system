class Person:
    def __init__(self, name, id):
        self.name = name
        self.__id = id   # private

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        if new_id:
            self.__id = new_id
        else:
            print("Invalid ID")

    def display_details(self):
        print("Name:", self.name)
        print("ID:", self.__id)
