# Student Grades Management System

This Python program manages a simple student grades database. Users can add, update, delete, and view students' grades through an interactive command-line interface.

## Features

- **Add Student**: Add a student's name and grade to the database.
- **Update Student**: Update an existing student's grade.
- **Delete Student**: Remove a student from the database.
- **View Students**: Display all students and their grades.
- **Exit**: Close the program.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Running the Program

1. Save the code to a file, e.g., `student_grades.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the program using:
   ```bash
   python student_grades.py
   ```

### Using the Program

1. Choose an option by entering the corresponding number:
   - `1`: Add a student by entering their name and grade.
   - `2`: Update an existing student's grade.
   - `3`: Delete a student.
   - `4`: View all students and their grades.
   - `5`: Exit the program.
2. Follow the prompts for each option to interact with the database.

## Code Structure

- **`students_grades`**: Dictionary storing student names as keys and grades as values.
- **`add_student`**: Adds a new student with a specified grade.
- **`update_student`**: Updates the grade for an existing student.
- **`delete_student`**: Removes a student from the database.
- **`display_all_students`**: Displays all students and their grades.
- **`main`**: Contains the main loop for user interaction.

## Example Usage

```
Student Grades Management System
1. Add Student
2. Update Student
3. Delete Student
4. View Students
5. Exit

Enter your choice: 1
Enter student name: John Doe
Enter student grade: 85
Added John Doe with a grade of 85.

Enter your choice: 4
John Doe: 85
```

## Error Handling

- **Invalid Input**: If non-numeric input is entered for grade or menu choice, an error message is displayed.
- **Non-existent Students**: If a user attempts to update or delete a non-existent student, an appropriate message is shown.

---

This README provides a concise overview of the Student Grades Management System, allowing users to understand the functionality and usage of the program quickly.
