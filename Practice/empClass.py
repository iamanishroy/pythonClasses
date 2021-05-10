class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def displayDelails(self):
        print('|---------------------------|')
        print('|')
        print('|    Name   ->', self.name)
        print('|    age    ->', self.age)
        print('|    salary ->', self.salary)
        print('|    gender ->', 'male' if self.gender == 'M' else 'female')
        print('|')
        print('|---------------------------|', '\n')


e1 = Employee('Sonu', 33, 40000, 'M')
e1.displayDelails()

e2 = Employee('Bijay', 36, 46000, 'M')
e2.displayDelails()

e3 = Employee('Annam', 40, 50000, 'F')
e3.displayDelails()

e4 = Employee('Rimta', 32, 42000, 'F')
e4.displayDelails()

e5 = Employee('Ashish', 30, 42500, 'M')
e5.displayDelails()
