
# Access Modifiers in python.

# Types:
# 1. Public
class Employee:
    def __init__(self):
        self.name="Pramod"

a=Employee()
print(a.name)



# 2.Private
class Employee:
    def __init__(self):
        self.__name="Pramod"

a=Employee()
# print(a.__name) # cannot be accessed directly.
print(a._Employee__name) # Can be accessed indirectly. concept of Name mangling.



# 3.Protected
class Employee:
    def __init__(self):
        self._name="Pramod"

a=Employee()
# print(a.__name) # cannot be accessed directly.
print(a._name) # Can be accessed indirectly.