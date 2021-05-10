class Parent:
    def show(self):
        print('Parent')


class Child(Parent):
    def display(self):
        print('Child')


c = Child()
c.display()
c.show()

# single 1 -> 2
# multilevel 1 -> 2 -> 3
# hierarchical 1 -> | -> 2 | 3
# multiple 1 | 2 -> | -> 3

