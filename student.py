class Student:
    def __init__(self, student_id, name, year):
        self.student_id = student_id
        self.name = name
        self.year = year

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Year: {self.year}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, year):
        student = Student(student_id, name, year)
        self.students.append(student)
        print("Student added successfully!")

    def show_students(self):
        if not self.students:
            print("No students in the list.")
            return
        for s in self.students:
            print(s)


def main():
    manager = StudentManager()

    while True:
        print("\n=== STUDENT MANAGEMENT ===")
        print("1. Add student")
        print("2. Show all students")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            year = input("Year: ")
            manager.add_student(sid, name, year)
        elif choice == "2":
            manager.show_students()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
