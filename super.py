class shape:
    def __init__(self, color, is_filled):
        self.color=color
        self.is_filled=is_filled
    
    def describe(self):
        print(f"this is {self.color} and {'filled' if self.is_filled else 'Not filled'}")

class circle(shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius=radius
    
    def describe(self):
        print(f"It is a circle with {self.radius} and area = {3.14*self.radius*self.radius}")

class square(shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width=width
    def describe(self):
        print(f"Area= {self.width*self.width}")
        
class triangle(shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width=width
        self.height=height
    def describe(self):
        print(f"Area= {self.width * self.height/2}")


Cri=circle(color="Blue", is_filled=True, radius=5)
squ=square(color="yellow", is_filled=True, width=4)
tri=triangle(color="yellow", is_filled=False, width=10, height=10)

print(tri.color)
print(tri.is_filled)
print(f"{tri.width}cm")
print(f"{tri.height}cm")


squ.describe()
        