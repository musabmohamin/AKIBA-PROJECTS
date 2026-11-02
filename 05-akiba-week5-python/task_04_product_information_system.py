class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
       return f"Product Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    def total_value(self):
        return self.price * self.quantity

p1 = Product("Laptop", 1000, 5)
p2 = Product("Smartphone", 500, 10)
p3 = Product("Tablet", 300, 7)
print(p1)
print(p2)
print(p3)
print(f"Total value of {p1.name}: {p1.total_value()}")