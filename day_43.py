
# Map,Filter and Reduce


# Map
def cube(x):
    return x*x*x
print(cube(2))


l=[1,3,4,6,7,5,3]
# newl=[]
# for item in l:
#     newl.append(cube(item))

newl=list(map(cube,l))
print(newl)




# Filter
def filter_function(a):
    return a>4

newnewl=list(filter(filter_function,l))
print(newnewl)

# Using lambda
newnewl=list(filter(lambda x: x%2==0,l))
print(newnewl)




# Reduce
from functools import reduce
# list of numbers
numbers=[1,2,3,4,5]
# Calculate the sum of the numbers using the reduce function.
sum=reduce(lambda x,y:x+y,numbers)

print(sum)