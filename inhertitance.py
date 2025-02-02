class Animal:
    def __init__(self, name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is Sleeping")


class Dog(Animal):
    def speak(self):
        print("Bark")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Mouse(Animal):
    def speak(self):
        print("chew")

dog=Dog("Doggy")
cat=Cat("kittu")
mouse=Mouse("Mpsly")

print(dog.name)
print(mouse.is_alive)
mouse.eat()
cat.sleep()
dog.speak()
cat.speak()
mouse.speak()