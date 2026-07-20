import json
import os

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def load_students():
    with open("students.json", "r") as file:
        return json.load(file)

def show_menu():
    print("\n" + "=" * 35) 
    print("     STUDENT MANAGEMENT SYSTEM")
    print("=" * 35)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

if os.path.exists("students.json"):
    students = load_students()
else:
    students = []

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        print("Adding a new student...")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        branch = input("Enter student branch: ")
        student = {
            'name': name,
            'age': age,
            'branch': branch
        }
        students.append(student)
        save_students()
        print("Student added successfully!")

    elif choice == '2':
        print("Viewing all students...")
        if len(students) == 0:
            print("No students found.")

        else:
            for i, student in enumerate(students, start=1):
                print(f"\nStudent {i}")
                print(f"Name   : {student['name']}")
                print(f"Age    : {student['age']}")
                print(f"Branch : {student['branch']}")
                print("-" * 30)

    elif choice == '3':
        print("Searching for a student...")
        name = input("Enter student name to search: ")
        name = name.lower()
        found = False
        for i, student in enumerate(students, start=1):
            if name in student["name"].lower():
                print(f"\nSearch Result {i}")
                print(f"Name   : {student['name']}")
                print(f"Age    : {student['age']}")
                print(f"Branch : {student['branch']}")
                print("-" * 30)
                found = True
        
        if not found:
            print("Student not found.")

    elif choice == '4':
        print("Deleting a student...")
        name = input("Enter student name to delete: ")
        name = name.lower()
        found = False
        for i, student in enumerate(students):
            if name in student["name"].lower():
                del students[i]
                print("Student deleted successfully!")
                found = True
                save_students()
                break
        if not found:
            print("Student not found.")
    
    elif choice == '5':
        print("Updating a student...")
        name = input("Enter student name to update: ")
        name = name.lower()
        found = False
        for student in students:
            if name in student["name"].lower():
                new_name = input("Enter new name (Leave blank to keep current): ")
                new_age = input("Enter new age (Leave blank to keep current): ")
                new_branch = input("Enter new branch (Leave blank to keep current): ")
                if new_name:
                    student["name"] = new_name
                if new_age:
                    student["age"] = int(new_age)
                if new_branch:
                    student["branch"] = new_branch

                print("Student updated successfully!")
                found = True
                save_students()
                break

        if not found:
            print("Student not found.")

    elif choice == '6':
        print("Exiting the program...")
        save_students()
        break

    else:
        print("Invalid choice. Please try again.")
   