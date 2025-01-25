name="thanya"
age=21
gpa= 7.5
student= True


print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# explicit typeCasting
name=bool(name)
age=float(age)
gpa=int(gpa)
student=str(True)

print(type(name))
print(name)

print(type(age))
print((age))

print(type(gpa))
print((gpa))

print(type(student))
print((student))


# implicit
x=2
y=2.3

x=x*y
print(x)