class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, details):
        return cls(details.split("-")[0], int(details.split("-")[1]))

e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

details = "Aseem-25000"
e2 = Employee(details.split("-")[0], int(details.split("-")[1]))
print(e2.name)
print(e2.salary)

string = "John-30000"
e3 = Employee.fromStr(string)
print(e3.name)
print(e3.salary)