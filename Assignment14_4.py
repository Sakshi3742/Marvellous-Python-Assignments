class Student:
    school_name = "ABC School"

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School Name: {Student.school_name}")

student1 = Student("Riya", 1)
student2 = Student("Pooja", 2)

student1.display()
student2.display()

Student.school_name = "XYZ School"

student1.display()
student2.display()