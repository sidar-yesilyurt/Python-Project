# main.py
# Import all necessary modules and classes
from student_operations import add_student, delete_student, update_student, list_students
from storage import save_students, load_students
from models.student import Student
from models.undergraduate import Undergraduate
from exceptions import InvalidIDException, DuplicateStudentIDException

def main():
    # Load existing student data from file
    students = load_students()
    
    # Main program loop - runs until user chooses to exit
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. List Students")
        print("5. Exit")
        
        # Get user's menu choice
        choice = input("Enter your choice: ")

        # Option 1: Add a new student
        if choice == "1":
            try:
                # Collect student information from user
                student_id = input("Enter Student ID: ")
                name = input("Enter Name: ")
                course = input("Enter Course: ")
                year = input("Enter Year: ")
                minor = input("Enter Minor (if undergraduate, else leave blank): ")
                
                # Create appropriate student object based on minor input
                if minor:
                    student = Undergraduate(student_id, name, course, year, minor)
                else:
                    student = Student(student_id, name, course, year)
                
                # Attempt to add student and show result
                if add_student(students, student):
                    print("Student added successfully!")
                else:
                    print("Failed to add student.")
                    
            # Handle specific exceptions that might occur
            except (InvalidIDException, DuplicateStudentIDException) as e:
                print(f"Error: {e}")

        # Option 2: Delete an existing student
        elif choice == "2":
            student_id = input("Enter Student ID to delete: ")
            if delete_student(students, student_id):
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        # Option 3: Update a student's course
        elif choice == "3":
            student_id = input("Enter Student ID to update: ")
            new_course = input("Enter new course: ")
            if update_student(students, student_id, new_course):
                print("Student updated successfully!")
            else:
                print("Student not found.")

        # Option 4: List all students
        elif choice == "4":
            students_list = list_students(students)
            for student in students_list:
                print(student)

        # Option 5: Exit the program
        elif choice == "5":
            save_students(students)  # Save data before exiting
            print("Exiting...")
            break

        # Handle invalid menu choices
        else:
            print("Invalid choice. Please try again.")

# Standard Python idiom to run main() when executed directly
if __name__ == "__main__":
    main()