class Circle:
    def __init__(self, r):
        self.radius = r

    def getArea(self):
        return 22/7 * self.radius**2

    def getCircumference(self):
        return 2 * (22/7) * self.radius


c1 = Circle(5)
print(c1.getArea())
print(c1.getCircumference())
