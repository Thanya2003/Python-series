from abc import ABC, abstractmethod  
class shape:

    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return 3.14*(self.radius**2)
    
class square(shape):
    def __init__(self, sides):
        self.sides=sides

    def area(self):
        return (self.sides**2)
    
class triangle(shape):
    def __init__(self, base, height):
        self.base=base
        self.height=height

    def area(self):
        return self.base * self.height * 0.5

class pizza(circle):
    def __init__(self, toppings, radius):
        super().__init__(radius) 
        self.toppings= toppings   
shapes=[circle(4), square(5), triangle(4,6), pizza("pepperoni", 10) ]
for i in shapes:
    print(f"{i.area()} cm²")
        