x = [1, 2, 3]
print(dir(x)) #Prints all the methods which can be performed on list.
print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
p = Person("Harry", 19)
print(p.__dict__) #Prints the dictionary containing of all the attributes of the class.
print(help(Person))