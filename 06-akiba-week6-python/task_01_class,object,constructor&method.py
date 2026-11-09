
# ==========================================
# QUESTION 1: CLASSES, OBJECTS, CONSTRUCTORS,
# AND METHODS
# ==========================================


class Student:
 
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    # Instance method to display student information
    def display_info(self):
        print("Student Information")
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Department:", self.department)

    # Instance method to introduce the student
    def introduce(self):
        print(f"Hello! My name is {self.name}. "
              f"I study {self.department}.")



student1 = Student("Musa", 101, "Computer Engineering")
student2 = Student("Ahmed", 102, "Electrical Engineering")
student3 = Student("Sara", 103, "Software Engineering")



student1.display_info()
student1.introduce()

print("------------------------------")

student2.display_info()
student2.introduce()

print("------------------------------")

student3.display_info()
student3.introduce()


# ==========================================
# THEORETICAL QUESTIONS AND ANSWERS
# ==========================================

# Q1. What is a class in Python?
# A class is a blueprint or template used to create objects.
# It defines the attributes and methods that objects will have.


# Q2. What is an object?
# An object is an instance of a class.
# It contains its own data and can use the methods defined
# in the class.
# Example: student1, student2, and student3 are objects
# of the Student class.


# Q3. What is the purpose of the __init__() method?
# The __init__() method is a constructor that initializes
# the attributes of an object when it is created.
# It is automatically called when a new object is created.


# Q4. What is the difference between an attribute and a method?
# An attribute is a variable that stores data or information
# about an object, while a method is a function defined
# inside a class that performs an action.
# Example:
# Attribute: self.name
# Method: display_info()
