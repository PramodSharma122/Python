
# Local variable and global variable:


x=40 # Global variable

def hello():
    global x
    x=4 # this will change the value of the global variable x
    y=5 # local variable
    print(y)

hello()
print(x)
# print(y) #this will cause an error because y is a local variable and is not accessible outside of the function.