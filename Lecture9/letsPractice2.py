'''
Define a Employee class with attributes role, department & salary.
This class also has a showDetails() method.
Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.
'''

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(self.role)
        print(self.department)
        print(self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75.000")

# el = Employee("accountant", "Finance", "60,000")
# el.showDetails()

engg1 = Engineer("Elon Must", 40)
engg1.showDetails()