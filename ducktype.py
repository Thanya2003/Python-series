class Animal:
    alive = True
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class CaT(Animal):
    def speak(self):
        print("MEOW!")

class car:
    alive=False

    def speak(self):
        print("HORN!.")

Animals= [Dog(), CaT(), car()]

for animal in Animals:
    animal.speak()
    print(animal.alive)