students_grades = {}

def add_student(name, grade):
    students_grades[name] = grade
    print(f"Added {name} with a grade of {grade}.")

def update_student(name, grade):
    if name in students_grades:
        students_grades[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in students_grades:
        del students_grades[name]
        print(f"{name} has been successfully deleted.")
    else:
        print(f"{name} is not found!")

def display_all_students():
    if students_grades:
        for name, grade in students_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found/added.")

def main():
    while True:
        print('\nStudent Grades Management System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        if choice == 1:
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter student grade: "))
            except ValueError:
                print("Please enter a valid grade!")
                continue
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter new grade: "))
            except ValueError:
                print("Please enter a valid grade!")
                continue
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("Closing the program...")
            break
        else:
            print("Invalid Choice!")

if __name__ == '__main__':
    main()
