class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def display_details(self):
        print("Name:",self.name)
        print("ID:",self.id)