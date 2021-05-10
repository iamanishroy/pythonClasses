class Shape(object):
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color


class Rectangle(Shape):
    def __init__(self, color, length, breadth):
        Shape.__init__(self, color)
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth


class Circle(Shape):
    def __init__(self, color, radius):
        Shape.__init__(self, color)
        self.radius = radius

    def getArea(self):
        return (22/7) * self.radius**2


class Triangle(Shape):
    def __init__(self, color, base, height):
        Shape.__init__(self, color)
        self.base = base
        self.height = height

    def getArea(self):
        return (1/2) * self.base * self.height


rect = Rectangle('blue', 12, 10)
print(rect.getColor(), rect.getArea())

circ = Circle('yellow', 5)
print(circ.getArea())
print(circ.getColor(), circ.getArea())

tri = Triangle('green', 6, 10)
print(tri.getColor(), tri.getArea())
