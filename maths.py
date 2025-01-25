# bulit in function
 

x=3.143555
y=-54
# res=math.sqrt(100)
z=8.1

res=round(x, 2)
res=abs(y)
res=pow(z, 2)
res=max(x, y, z)
res=min(x, y, z)


# Math function
import math
res=math.sqrt(100)
res=math.pi
res=math.e
res=math.ceil(z)
res=math.floor(z)

# excerise 1 cricumference of the circle
# radius=float(input("what is the Radius of the circle "))

# cricuference = round(2*math.pi*radius,3)

# print(f"The Cricumference of the Circle is {cricuference}cm")




# Excerise 2 Area of the circle
# radius=float(input("what is the Radius of the circle "))
# area=round(math.pi*pow(radius, 2), 3)
# print(f"The Area of the Circle is {area}")

# exercise 3 3rd side of the right angled triangle

A=float(int(input("What is A side of the Triangle ")))
B=float(int(input("What is B side of the Triangle ")))

C=round(math.sqrt(pow(A,2)+pow(B,2)), 3)

print(f"Length of the side C {C}")