
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle {self.width}x{self.height}"


# Create three rectangle objects
rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 6)
rect3 = Rectangle(2, 8)

# Print rectangles and their areas
print(rect1)
print("Area:", rect1.area())

print(rect2)
print("Area:", rect2.area())

print(rect3)
print("Area:", rect3.area())
