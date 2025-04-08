from models.student import Student
from models.undergraduate import Undergraduate
from exceptions import InvalidIDException, DuplicateStudentIDException

def validate_student_id(students, student_id):
    # Check if student ID is unique
    for student in students:
        if student.get_student_id() == student_id:
            return False
    return True

def add_student(students, student):
    """Adds a new student to the system after validation.
    
    Args:
        students: List of existing students
        student: New student to add
        
    Returns:
        bool: True if student was added successfully
        
    Raises:
        InvalidIDException: If student ID is empty
        DuplicateStudentIDException: If student ID already exists
    """
    # Validate student ID is not empty
    if not student.get_student_id():
        raise InvalidIDException("Student ID cannot be empty")
    
    # Check if student ID is unique
    if not validate_student_id(students, student.get_student_id()):
        raise DuplicateStudentIDException("Student ID already exists")
    
    # Add the valid student to the list
    students.append(student)
    return True


def delete_student(students, student_id): #Removes a student from the system by their ID.

    # Search through all students
    for student in students:
        # Check if current student matches the ID
        if student.get_student_id() == student_id:
            # Remove the matching student
            students.remove(student)
            return True
    
    # Return False if no matching student found
    return False


def update_student(students, student_id, new_course): #Updates a student's course information.
    # Search through all students
    for student in students:
        # Check if current student matches the ID
        if student.get_student_id() == student_id:
            # Update the course information
            student.update_course(new_course)
            return True
    
    # Return False if no matching student found
    return False


def list_students(students): #Returns a list of all students' details.
    # Create and return a list of student details dictionaries
    return [student.get_details() for student in students]