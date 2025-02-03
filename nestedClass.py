class Company:
    class Employee:
        def __init__(self, name, position):
            self.name=name
            self.position=position
        
        def get_details(self):
            return f"{self.name} {self.position}"
        
    def __init__(self, company_name):
        self.company_name=company_name
        self.employeess=[]

    def add_employee(self, name, position):
        newEmployee=self.Employee(name, position)
        self.employeess.append(newEmployee)
    
    def list_emp(self):
        return[empy.get_details() for empy in self.employeess]

company=Company("Thanya Foods")

company.add_employee("Thanya", "thar")
company.add_employee("Dhanya", "React")

for empy in company.list_emp():
    print(empy)       