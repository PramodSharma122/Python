
# Lambda functions in python:

def hello(fx,value):
    return 7+fx(value)



double=lambda x: x*2
cube =lambda x: x*x*x
avg=lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(3))
print(avg(3,4,5))
print(hello(lambda x: x*x*x,2))