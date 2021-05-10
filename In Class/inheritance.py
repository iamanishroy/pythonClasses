class Person(object):
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name


class Student(Person):
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)


class Teacher(Person):
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "%s teachers %s" % (self.name, ','.join(self.papers))
