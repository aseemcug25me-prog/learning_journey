class Employee:
    company = 'Apple'
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
    @classmethod     #It changes the class variable. Earlier name was given to instance or object.
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Aseem"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)