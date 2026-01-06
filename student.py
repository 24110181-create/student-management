import csv
import os

class Student:
    def __init__(self, student_id, name, year):
        self.student_id = student_id
        self.name = name
        self.year = year

    def to_list(self):
        return [self.student_id, self.name, self.year]

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Year: {self.year}"


class StudentManager:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    self.students.append(Student(row[0], row[1], row[2]))

    def save_to_file(self):
        with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for s in self.students:
                writer.writerow(s.to_list())

    def add_student(self, student_id, name, year):
        self.students.append(Student(student_id, name, year))
        self.save_to_file()
        print("Student added and saved!")

    def show_students(self):
        if not self.stude
