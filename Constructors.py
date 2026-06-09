class Student:
    def __init__(self, rollno, name, total_marks):
        self.rollno = rollno
        self.name = name
        self.total_marks = total_marks
    def display(self):
        print(f"Roll No: {self.rollno}, Name: {self.name}, Total Marks: {self.total_marks}")
    def grade(self):
        if self.total_marks >= 90:
            return "A"
        elif self.total_marks >= 80:
            return "B"
        elif self.total_marks >= 70:
            return "C"
        elif self.total_marks >= 60:
            return "D"
        else:
            return "F"
s1 = Student(2501001, "Suraj Chauhan", 95)
s2 = Student(2501002, "Aseem Krishna Choudhary", 85)
s3 = Student(2501003, "Mohit Singh", 90)
s4 = Student(2501004, "Aryan Singh", 65)
s1.display()
print(f"Grade: {s1.grade()}")
s2.display()
print(f"Grade: {s2.grade()}")
s3.display()
print(f"Grade: {s3.grade()}")
s4.display()
print(f"Grade: {s4.grade()}")