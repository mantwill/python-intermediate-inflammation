import math

class Shape:
    def __init__(self, colour):
        self.colour = colour
    @property
    def area(self):
        raise NotImplementedError("Subclasses must implement the area property.")

class Circle(Shape):
    def __init__(self, radius, colour):
        super().__init__(colour)    
        self.radius = radius
    
    @property
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height, colour):
        super().__init__(colour)
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, a,b,c, colour):
        super().__init__(colour)
        self.a = a
        self.b = b
        self.c = c
    @property
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Square(Rectangle):
    def __init__(self, side_length, colour):
        super().__init__(side_length, side_length, colour)


shapes = [
    Circle(5, "red"),
    Rectangle(4, 6, "red"),
    Square(3, "red"),
    Triangle(3, 4, 5, "red"),
]

[print(shape.area) for shape in shapes]
[print(shape.colour) for shape in shapes]
