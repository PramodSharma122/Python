
# Python Decorators


def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx
@greet

def hello():
    print("Hello world")

hello()



def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

def add(a,b):
    print(a+b)

greet(add)(3,5)