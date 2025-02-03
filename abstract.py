from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass


class car(vehicle):
    def go(self):
        print("car is driving")

    def stop(self):
        print("Stop the car")

class Bus(vehicle):
    def go(self):
        print("Bus is driving")

    def stop(self):
        print("Stop the Bus")

class Boat(vehicle):
    def go(self):
        print("Boat is driving")

    def stop(self):
        print("Stop the Boat")

Car=car()
Car.go()
Car.stop()

boat=Boat()
boat.go()
boat.stop()

bus=Bus()
bus.go()
bus.stop()