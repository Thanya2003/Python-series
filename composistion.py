class Engine:
    def __init__(self, horse_power):
        self.horse_power=horse_power

class Wheel_car:
    def __init__(self, size):
        self.size=size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make=make
        self.model=model
        self.engine= Engine(horse_power)
        self.wheel=[Wheel_car(wheel_size) for wheel in range(4)]

    def print_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}hp {self.wheel[0].size}in"

car=Car(make="Ford", model="Mustard", horse_power="335watt", wheel_size="18")

print(car.print_car())