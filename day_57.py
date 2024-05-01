
# Dunder or Magic methods in Python

class Employee:
    name="Pramod"
    def __len__(self):
        i=0
        for item in self.name:
            i=i+1
        return i
    
    # __str__ methods
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    
    # __repr__ methods
    def __repr__(self):
        return f"Employee('{self.name}')"
    
    # __call_ methods
    def __call__(self):
        print("Hey,I am good")


e=Employee()
print(e.name)

print(str(e))
print(repr(e))
e()

print(len(e))