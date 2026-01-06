class Student:
    def __init__(self, student_id, name, year):
        self.student_id = student_id
        self.name = name
        self.year = year

    def to_list(self):
        return [self.student_id, self.name, self.year]

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Year: {self.year}"
