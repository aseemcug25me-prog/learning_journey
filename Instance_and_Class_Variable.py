class Employee:
    companyName = "Apple" # Class Variable
    def __init__(self, name):
        self.name = name # Instance Variable
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and his raise amount in {self.companyName} is {self.raise_amount}")

emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.showDetails()
emp2 = Employee("Aseem")
emp2.showDetails()