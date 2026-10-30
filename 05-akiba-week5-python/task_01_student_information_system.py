
class Students:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)


s1 = Students("Musab", 20, "Information Science")
s2 = Students("Inaya", 18, "Medicine")
s3 = Students("Nizam", 24, "Governance")

s1.display_info()
s2.display_info()
s3.display_info()
