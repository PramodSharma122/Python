
# Getters

class Myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"value is {self._value}")
    
    @property
    def value(self):
        return 10*self._value
    
obj=Myclass(10)
print(obj.value)
obj.show()



# Setters

class Myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"value is {self._value}")
    
    @property
    def value(self):
        return 10*self._value
    
    @value.setter
    def ten_value(self,new_value):
        self._value=new_value/10
    
obj=Myclass(10)
obj.ten_value=85
print(obj.ten_value)
obj.show()