import json
from student import Student


def save_students(students):

    student_data = []

    for student in students:
        student_data.append(student.to_dict())

    with open("students.json", "w") as file:
        json.dump(student_data, file, indent=4)


def load_students():

    try:
        with open("students.json", "r") as file:
            data = json.load(file)

            students = []

            for item in data:
                students.append(Student.from_dict(item))

            return students

    except FileNotFoundError:
        return []