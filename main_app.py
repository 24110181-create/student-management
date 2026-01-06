from manager import StudentManager


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
            print("Student added!")
        elif choice == "2":
            manager.show_students()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
