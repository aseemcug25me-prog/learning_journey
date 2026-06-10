class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def show(self):
        print(f"The name of the Employee is {self.name}")
        print(f"{self.name} id is {self.id}")
class Programmer(Employee):
    def showLang(self):
        print("Python is the default Language")
e1 = Employee("Aseem Bhai", 2501002)
e1.show()
e2 = Programmer("Kamran Bhai", 2501001)
e2.show()
e2.showLang()