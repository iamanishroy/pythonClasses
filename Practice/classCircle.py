class Circle:
    def __init__(self, r):
        self.radius = r
        pass

    def getArea(self):
        return 22/7 * self.radius**2


c1 = Circle(5)
c2 = Circle(15)
c3 = Circle(25)
print(c1.getArea())
print(c2.getArea())
print(c3.getArea())
