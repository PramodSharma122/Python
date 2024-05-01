
# OOPs in python.

# RailwayForm ---> class [blueprint]
# pramod ---> pramod ko info wala form --> Object [entity]
# Ram ---> ram ko info wala form --> Object [entity]


# Class and object in python.

class Person:
    name="Pramod"
    occupation="Software dev."
    networth=10

a=Person()
print(a.name,a.occupation)



class Person:
    name="Pramod"
    occupation="Software dev."
    networth=10

a=Person()
a.name="Prem"
a.occupation="Web dev."
print(a.name,a.occupation)


# Using Self parameter
class Person:
    name="Pramod"
    occupation="Software dev."
    networth=10

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
a.info()