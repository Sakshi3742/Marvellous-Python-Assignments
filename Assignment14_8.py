class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        print("Car with additional behaviour")

obj1 = Vehicle()
obj1.start()

obj2 = Car()
obj2.start()