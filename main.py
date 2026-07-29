from student import Student
from database import save_students, load_students

students = load_students()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Branch")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        branch = input("Enter Branch: ")

        student = Student(name, age, branch)

        students.append(student)

        save_students(students)

        print("Student added successfully!")


    elif choice == "2":
        
        if len(students) == 0:
            print("No students found.")
            
        else:
            print("\n===== Student List =====")
            for student in students:
                print("--------------------")
                student.display()

    elif choice == "3":
        
        search_name = input("Enter student name to search: ")
        found = False
        for student in students:
            if student.name.lower() == search_name.lower():
                print("--------------------")
                student.display()
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        
        search_name = input("Enter student name to update branch: ")
        found = False
        
        for student in students:
            if student.name.lower() == search_name.lower():
                new_branch = input("Enter new branch: ")
                student.update_branch(new_branch)
                save_students(students)
                print("Branch updated successfully!")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "5":
        
        search_name = input("Enter student name to delete: ")
        found = False
        
        for student in students:
            if student.name.lower() == search_name.lower():
                students.remove(student)
                save_students(students)
                print("Student deleted successfully!")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "6":
        print("Thank you for using the Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice!")