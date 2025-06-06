class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self._department = department
        self.__salary = salary

    def details(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)

emp1 = Employee("Rohit", 50000, "IT")

print("Public Name:",emp1.name)
print("Protected Department:",emp1._department)
print("Private Salary:",emp1._Employee__salary)
emp1.details()