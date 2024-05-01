
# Inheritance in python.

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showDetails(self):
        print(f"The name of employee: {self.id} is {self.name}")

class programmer(Employee):
    def showLang(self):
        print("The default language is Python")

e1=Employee("Pramod",400)
e1.showDetails()
e2=programmer("Hari",700)
e2.showDetails()
e2.showLang()