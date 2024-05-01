
# Function arguments in Pythons

def average(a=9,b=1):
    print("The average is ", (a+b)/2)

average()


# default argument:
def average(a=9,b=1):
    print("The average is ", (a+b)/2)

average(6)
average(b=4)
average(b=5,a=3) # keyword arguments:



# Required argument:
def average(a,b=1):
    print("The average is ", (a+b)/2)

average(6)

def average(a,b,c=1):
    print("The average is ", (a+b+c)/2)

average(5,6)



# Variable-length arguments:
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is: ",sum/len(numbers))

average(6,5,7,1)




# Keywords Arbitrary Arguments:
def name(**name): # (** is dictionary)
    print(type(name))
    print("Hello,",name["fname"],name["mname"],name["lname"])

name(mname="Bahadur",lname="Sharma",fname="Prakash")




# Return statement:
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

avg=average(6,5,7,1)
print(avg)