class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(5.0, 3.0)
print("Area:", rectangle1.area())  # Output: 15.0
print("Perimeter:", rectangle1.perimeter())  # Output: 16.0