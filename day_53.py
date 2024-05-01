
# Python Class Methods

class Class:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod  # Using class method
    def changeCompany(cls,newCompany):
        cls.company=newCompany

e1=Class()
e1.name="Pramod"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Class.company)