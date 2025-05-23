class Student:
    # The __init__ method is called when a new Student object is created
    def __init__(self, student_id, name, course, year):
        # Initialize the student's attributes as private variables
        self.__student_id = student_id  # Unique identifier for the student
        self.__name = name              # Student's full name
        self.__course = course          # Course the student is enrolled in
        self.__year = year              # Current year of study 

    # Getter methods - allow access to private attributes from outside the class
    
    def get_student_id(self):
        """Returns the student's ID"""
        return self.__student_id

    def get_name(self):
        """Returns the student's name"""
        return self.__name

    def get_course(self):
        """Returns the student's course"""
        return self.__course

    def get_year(self):
        """Returns the student's current year of study"""
        return self.__year

    # Setter methods - allow modifying private attributes from outside the class
    
    def set_student_id(self, student_id):
        """Updates the student's ID"""
        self.__student_id = student_id

    def update_course(self, new_course):
        """Updates the student's course"""
        self.__course = new_course

    # Get details method
    
    def get_details(self):
        """Returns a dictionary with all the student's details
        Useful for displaying information or saving to a file"""
        return {
            "Student ID": self.__student_id,
            "Name": self.__name,
            "Course": self.__course,
            "Year": self.__year
        }