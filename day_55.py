
# dir, __dict__ and help methods in python


# The dir() method

x=[1,2,3,4]
print(dir(x))
print(x.__add__)



# The __dict__ method

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.verson=1

p=person("Prem",20)
print(p.__dict__)



# The help() method

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.verson=1

p=person("Prem",20)
print(p.__dict__)
print(help(person))