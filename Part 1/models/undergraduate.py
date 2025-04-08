
# Import the Student class that we'll inherit from
from models.student import Student

# Define the Undergraduate class
class Undergraduate(Student):
    def __init__(self, student_id, name, course, year, minor):
        # Call the parent class (Student) constructor first
        super().__init__(student_id, name, course, year)
        # Add the additional attribute specific to Undergraduates
        self.__minor = minor

    # Getter method for the minor attribute
    def get_minor(self):
        """Returns the student's minor field of study"""
        return self.__minor

    # Override the get_details method to include minor information
    def get_details(self):
        """Returns all student details including minor
        First gets the basic details from the parent class,
        then adds the minor information"""
        # Get the basic details from Student class
        details = super().get_details()
        # Add the minor information
        details["Minor"] = self.__minor
        return details