class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return "area=" ,self.length*self.width

    def perimeter(self):
        return "perimeter=", (2*self.length)+(2*self.width)

r1=Rectangle(2,3)
r2=Rectangle(4,8)
print(r1.area())
print(r2.area())
print(r1.perimeter())
print(r2.perimeter())
        