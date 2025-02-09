class student:
    count=0
    total_gpa=0
    def __init__(self, age, name, gpa):
        self.age=age
        self.name=name
        self.gpa=gpa
        student.count+=1
        student.total_gpa+=gpa

    def get_info(self):
        return f"{self.name} {self.name}"
    
    @classmethod
    def get_count(cls):
        return f"{cls.count}"
    
    @classmethod
    def get_average(cls):
        if student.count==0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count}"
    
student1=student(21, "Thanya", 3.4)
student2=student(11, "anya", 3.8)
student3=student(41, "dhanya", 4)
print(f"number of student {student.get_count()}")
print(f"Average GPA  of student {student.get_average()}")