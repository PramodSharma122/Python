
# sets methods in pythons

# Union
s={1,3,5,6,7}
s1={8,5,3,7,9,0}
print(s.union(s1))
s.update(s1)
print(s,s1)


# Intersection
s={1,3,5,6,7}
s1={8,5,3,7,9,0}
print(s.intersection(s1))
s.intersection_update(s1)
print(s)


# symmetric difference
s={1,3,5,6,7}
s1={8,5,3,7,9,0}
s2=s.symmetric_difference(s1)
print(s2)
print(s.symmetric_difference_update(s1))


# Difference
s={1,3,5,6,7}
s1={8,5,3,7,9,0}
s2=s.difference(s1)
print(s2)
print(s.difference_update(s1))


# isdisjoint() methods:
s={1,3,5,6,7}
s1={8,5,3,7,9,0}
s2=s.isdisjoint(s1)
print(s2)


# issuperset() methods:
s={1,3,5,6,7}
s1={8,5,3,7,9,0}
s2=s.issuperset(s1)
print(s2)


# issubset() methods:
s={1,3,5,6,7}
s1={8,5,3,7,9,0}
s2=s.issubset(s1)
print(s2)


# Add() methods:
s={1,3,5,6,7}
s.add("prem")
print(s)

# update() methods:
s={1,3,5,6,7}
s1={8,5,3,7,9,0}
s.update(s1)
print(s)


# Remove/Discard() methods:
s1={8,5,3,7,9,0}
s1.remove(9) # if not found the item showing the error
s1.discard(2) # if not found the item not showing the error
print(s1)


# Pop() methods:
cities={"Tokyo","Madrid","Nepal","Ktm"}
item=cities.pop()
print(cities)
print(item)


# # del methods:
# cities={"Tokyo","Madrid","Nepal","Ktm"}
# del cities
# print(cities)


# clear() methods:
cities={"Tokyo","Madrid","Nepal","Ktm"}
cities.clear()
print(cities)


# check if item exists
cities={"Tokyo","Madrid","Nepal","Ktm"}
if "Nepal" in cities:
    print("Nepal is present.")
else:
    print("Nepal is absent.")