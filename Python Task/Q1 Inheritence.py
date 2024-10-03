class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus1 = Bus("School Volvo", 180,12)


print(f"(Vehicle name : {bus1.name}, speed is {bus1.max_speed} and the mileage is {bus1.mileage})")