class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
    
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__(bodystyle = "Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed, "MPH")

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed, "MPH")

car1 = Car("gas")
car2 = Car("electric")
car2.drive(9999)
mc1 = Motorcycle("electric", True)
mc2 = Motorcycle("gas", False)
mc2.drive(3)

print(car1.wheels)
print(car2.enginetype)
print(mc1.wheels, mc1.enginetype)

