
# lists in python

l=[3,5,7,"pramod",True]
print(l)
print(type(l))
print(l[2]) 
print(l[3])
print(l[4]) # positive index
print(l[-3]) # negative index
print(l[:5])
print(l[1:6:2])


# same thing applies for strings as well!
if 7 in l:
    print("Yes")
else:
    print("No")

if "pra" in l:
    print("Yes")
else:
    print("No")



# list comprehension
List =[i*i for i in range(5)]
print(List)

list=[i for i in range(10) if i%2==0]
print(list)
