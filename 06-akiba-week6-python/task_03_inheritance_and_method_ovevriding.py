class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"


class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Programming Language: {self.programming_language}"


# Create objects
employee1 = Employee("Musab", 100)
manager1 = Manager("Ahmed", 200, "IT")
developer1 = Developer("Ali", 150, "Python")


# Display information
print(employee1.display_info())
print(manager1.display_info())
print(developer1.display_info())