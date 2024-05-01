
# Tuples of Pythons. Tuples are immutable we donot changing the tuple items.
# In tuples items want comma ',' and round brackets '()' are necessary.

tup=(1,5,6,"prem",True) 
print(type(tup),tup)
print(len(tup),tup)
print(tup[0])
print(tup[2])
print(tup[-2])

if 6 in tup:
    print("Yes 6 is present in this tuple")

tup2=tup[1:4]
print(tup2)