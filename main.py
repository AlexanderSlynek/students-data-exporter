import json
def get_students_data():
    students = []
    number_of_students = int(input("How many students do you want to add in this file: "))
    for i in range(number_of_students):
        student = []
        name = input("Input student's name: ")
        number_of_grades = int(input("How many grades does the student have: "))
        grades = []
        for j in range(number_of_grades):
            grade = input("Input student's grade: ")
            grades.append(grade)
        grades = ",".join(grades)
        student.append(name)
        student.append(grades)
        student = ",".join(student)
        students.append(student)
    students = "\n".join(students)
    return students
def export_to_txt():
    students = get_students_data()
    filename = input("What is going to be the name of the file: ")
    filename = filename + ".txt"
    with open(filename, "w", encoding = "utf-8") as f:
        f.write(students)
def export_to_csv():
    students = get_students_data()
    filename = input("What is going to be the name of the file: ")
    filename = filename + ".csv"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(students)
def export_to_json():
    students = get_students_data()
    filename = input("What is going to be the name of the file: ")
    filename = filename + ".json"
    students = students.replace("\n", " ")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f)
while True :
    print("1 - Export to TXT")
    print("2 - Export to CSV")
    print("3 - Export to JSON")
    print("4 - Exit")
    try:
        number = int(input("Input a number: "))
    except ValueError:
        print("It should be an integer")
        continue
    if (number == 1):
        export_to_txt()
    elif (number == 2):
        export_to_csv()
    elif (number == 3):
        export_to_json()
    elif (number == 4):
        print("Thank you for using this program")
        break
    else:
        print("This operation does not exist")
        continue
