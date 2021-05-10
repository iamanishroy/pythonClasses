class Computer:
    company = 'Lenovo'

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Config is: ', self.cpu, self.ram)

    def compare(self, other):
        return self.cpu == other.cpu

    @classmethod
    def getCompany(cls):
        return cls.company
    

    @staticmethod
    def info():
        print('info')


# super().__init_()

com1 = Computer('i5', '8gb')
com2 = Computer('i9', '16gb')

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()

print(com1.compare(com2))
print(Computer.compare(com1, com2))

print(id(com1))
print(id(com2))

print(Computer.getCompany())
Computer.info()
