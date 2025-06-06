class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary

    def display(self):
        super().display()
        print(f"Subject: {self.subject}, Salary: {self.salary}")

obj1 = Teacher("Usha",30, "Maths", 40000)
obj1.display()