
# Instance Vs Class Variables


class Employee:
    companyName="Apple"
    noOfEmployees=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        Employee.noOfEmployees+=1

    def showDetails(self):
        print(f"The name of Employee is{self.name} in {self.noOfEmployees} sized and {self.companyName} and the raise amount in {self.raise_amount}")

emp1=Employee("Pramod")
emp1.raise_amount=0.5
emp1.companyName="Apple US"
emp1.showDetails()

emp2=Employee("Sharma")
emp2.showDetails()

Employee.showDetails(emp1)