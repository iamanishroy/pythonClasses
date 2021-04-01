class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


# e = Example(8, 6)
# print(e.add())


class student(object):
    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year
        print("A student object is Created")

    def print_details(self):
        print("Name : ", self.name)
        print("Branch : ", self.branch)
        print("Year : ", self.year)


std1 = student('Vishal', 'BCA', '2021')
std1.print_details()
