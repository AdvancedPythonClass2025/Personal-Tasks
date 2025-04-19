class Shape:
    def area(self):

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  # محاسبه مساحت دایره

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # محاسبه مساحت مستطیل

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"مساحت دایره: {circle.area():.2f}")
print(f"مساحت مستطیل: {rectangle.area():.2f}")
