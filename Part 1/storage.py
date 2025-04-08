import os
from models.student import Student
from models.undergraduate import Undergraduate

def save_students(students, filename="Part 1/students.txt"): #Saves a list of student objects to a text file.
    try:
        # Open the file in write mode
        with open(filename, "w") as file:
            # Process each student in the list
            for student in students:
                # Check if student is an Undergraduate
                if isinstance(student, Undergraduate):
                    # Write undergraduate record with all fields including minor
                    file.write(
                        f"undergraduate|{student.get_student_id()}|{student.get_name()}|"
                        f"{student.get_course()}|{student.get_year()}|{student.get_minor()}\n"
                    )
                else:
                    # Write regular student record
                    file.write(
                        f"student|{student.get_student_id()}|{student.get_name()}|"
                        f"{student.get_course()}|{student.get_year()}|\n"
                    )
        return True
    
    except Exception as e:
        # Handle any errors that occur during file operations
        print(f"Error saving students: {e}")
        return False

def load_students(filename="students.txt"):
    students = []
    try:
        # Create file if it doesn't exist
        if not os.path.exists(filename):
            with open(filename, "w"):
                pass  # Just create empty file
            
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                    
                parts = line.split("|")
                if len(parts) < 5:  # Basic validation
                    continue
                    
                if parts[0] == "undergraduate":
                    if len(parts) < 6:
                        continue  # Skip incomplete records
                    student = Undergraduate(
                        parts[1],  # student_id
                        parts[2],  # name
                        parts[3],  # course
                        parts[4],  # year
                        parts[5]   # minor
                    )
                elif parts[0] == "student":
                    student = Student(
                        parts[1],  # student_id
                        parts[2],  # name
                        parts[3],  # course
                        parts[4]   # year
                    )
                else:
                    continue  # Skip invalid records
                    
                students.append(student)
        return students
    except Exception as e:
        print(f"Error loading students: {e}")
        return []