class Animal:
    def __init__(self, name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is Sleeping")
class prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class rabit(prey):
    pass
class hawk(predator):
    pass

class fish(prey, predator):
    pass
rab=rabit("rooww")
haw=hawk("haaa")
fi=fish("eel")

rab.sleep()
rab.eat()
haw.eat()
fi.sleep()
fi.hunt()