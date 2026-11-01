class Student:
    school="Akiba technology"
    def __init__ (self,name,score,department):
        self.name=name
        self.score=score
        self.department=department

    def display(self):
        return f"name:{self.name} score:{self.score} department: {self.department} school: {self.school}"

s1=Student("musab",89,"information science")
s2=Student("inaya",100,"medicine")
s3=Student("nizam",100,"goverance")
s2.score=97
print(s2.score)
print(s1.display())
print(s2.display())
print(s3.display())
print(Student.school)

# Question 1: What is the difference between a class attribute and an instance attribute?
#
# A class attribute is defined inside a class but outside the constructor.
# It is shared by all objects of that class.
# An instance attribute is defined using self inside the constructor.
# Each object has its own independent instance attributes.

# Question 2: Why does updating one student's score not automatically change the scores of other students?
#
# Each student object has its own score because score is an instance attribute.
# When I update one student's score, it only changes that particular object.
# The scores of other students remain unchanged because they have their own values.
