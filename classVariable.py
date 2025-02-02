class student:
    class_year=2025
    number_stud=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
        student.number_stud+=1

stude1=student("Thanya", 21)
stude2=student("Dhanya", 12)
stude3=student("Adhaya", 6)
stude4=student("Adhaya", 6)
stude5=student("Adhaya", 6)
stude6=student("Adhaya", 6)
stude7=student("Adhaya", 6)

print(f"My graudation class {student.class_year} batch contain {student.number_stud} students")
print(stude1.name)
print(stude2.name)
print(stude3.name)