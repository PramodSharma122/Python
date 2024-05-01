
# Constructors in python.


# Parameterized constructor
class person:
    def __init__(self,nam,oc):
        self.name=nam
        self.occ=oc

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("Pramod","Developer")
b=person("Aabri","Helper")
a.info()
b.info()




# Default Constructor 
class Details:
    def __init__(self):
        print("Animal Crab belongs to crustaceans group")

obj=Details()