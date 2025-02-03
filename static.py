class Employee:
    def __init__(self, name, position):
        self.name=name
        self.position=position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position=["manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position
    
emp1=Employee("Thanya", "manager")
emp2=Employee("Dhanya", "Cook")
emp3=Employee("Cashier", "Janitor")

print(Employee.is_valid_position("Cooker"))
print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())