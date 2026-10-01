class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_info(self):
        print(f"Student: {self.name}")
        print(f"Department: {self.department}")