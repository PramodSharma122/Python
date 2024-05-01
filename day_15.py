
# Functions in pythons

# User function
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater.")
    else:
        print("Second number is greater.")


# for pass
def isLesser(a,b):
    pass


a=9
b=8
c=4
d=7

isGreater(a,b) # calling a function
calculateGmean(a,b) # "" ""

isGreater(c,d)
calculateGmean(c,d)