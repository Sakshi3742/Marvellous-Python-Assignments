class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10,5)

area = rect.calculate_area()
perimeter = rect.calculate_perimeter()

print(f"Area: {area}, Perimeter: {perimeter}")
