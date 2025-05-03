# **Student Management System and Data Analysis Project**

## **Overview**

This project comprises two main parts:

* **Part 1: Student Management System** \- A system for managing student data using object-oriented programming.  
* **Part 2: Data Analysis System** \- A system for processing, analyzing, and visualizing messy data using Pandas, Seaborn, and Matplotlib.

## **Part 1: Student Management System**

### **Installation**

1. **Python:** Ensure you have Python 3.6 or later installed on your system. You can download it from [python.org](https://www.python.org/downloads/).  
2. **No external libraries are required:** This part of the project uses only standard Python libraries.

### **Usage**

1. **Download the project:** Download the project files and extract them to a directory on your computer.  
2. **Navigate to the project directory:** Open a terminal or command prompt and navigate to the directory where you extracted the project files.  
3. **Run the main program:** Execute the following command:  
   python main.py

4. **Interact with the menu:**  
   * The program will display a menu with options to:  
     * Add a student  
     * Delete a student  
     * Update a student's course  
     * List all students  
     * Exit the program  
   * Enter the number corresponding to your choice and follow the prompts.

### **File Structure**

* main.py: The main program file that provides the user interface for the Student Management System.  
* student.py: Defines the Student class.  
* undergraduate.py: Defines the Undergraduate class, which inherits from the Student class.  
* student\_operations.py: Contains functions to perform operations on student data (add, delete, update, list).  
* storage.py: Handles saving and loading student data from the students.txt file.  
* exceptions.py: Defines custom exception classes used in the program.  
* students.txt: A text file used to store student data.

### **Data Storage**

* Student data is stored in the students.txt file. Each line in the file represents a student record. The format of each line is:  
  * For a regular student: student|student\_id|name|course|year|  
  * For an undergraduate student: undergraduate|student\_id|name|course|year|minor

### **Assumptions**

* Student IDs are assumed to be unique. The program will raise an exception if you try to add a student with a duplicate ID.  
* Input validation is basic. The program expects input in the specified format.

## **Part 2: Data Analysis System**

### **Installation**

1. **Python:** Ensure you have Python 3.6 or later installed on your system. You can download it from [python.org](https://www.python.org/downloads/).  
2. **Install the required libraries:** This part of the project uses the Pandas, Seaborn, and Matplotlib libraries. You can install them using pip:  
   pip install pandas seaborn matplotlib

### **Usage**

1. **Download the project:** Download the project files and extract them to a directory on your computer.  
2. **Navigate to the project directory:** Open a terminal or command prompt and navigate to the directory where you extracted the project files.  
3. **Place the data file:** Ensure that the messy\_dataset.csv file is located in the same directory as the Python script.  
4. **Run the data analysis script:** Execute the following command:  
   python main.py

   * The script will:  
     * Load data from messy\_dataset.csv.  
     * Clean the data (handle missing values, remove duplicates, etc.).  
     * Analyze the data.  
     * Generate visualizations (histograms, scatter plots, bar charts).  
     * Save the cleaned data to a new file (if the script includes that functionality).

### **File Structure**

* main.py: The main program file that contains the data analysis script.  
* messy\_dataset.csv: The CSV file containing the messy data to be analyzed.

### **Data Handling**

* The script reads data from messy\_dataset.csv.  
* The script performs data cleaning operations, including:  
  * Handling missing values (imputation with mean for numerical columns, dropping rows for categorical columns).  
  * Removing duplicate rows.  
  * Filtering outliers using the IQR method.  
* The script generates visualizations to help understand the data, including:  
  * Histogram of Sales.  
  * Scatter plot of Sales vs Profit.  
  * Bar chart of Total Sales by Category.  
* The cleaned data may be saved to a new CSV file. Check the script for the specific filename.

### **Assumptions**

* The script assumes that the messy\_dataset.csv file exists in the same directory as the script.  
* The script is designed to handle the specific data format and issues present in the provided messy\_dataset.csv file. It may need to be modified to work with different datasets.