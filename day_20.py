
# Manipulating Tuples


countries=("span","italy","India","england","nepal")
temp=list(countries)
temp.append("Russia")   # add item
temp.pop(3)             # remove item
temp[2]="Finland"       # change item
countries=tuple(temp)
print(countries)

# mearge the two tuple
countries2=("Vietnam","bharatpur","pokhara")
con=countries+countries2
print(con)


# Tuple methods:
tuple1=(0,4,5,6,2,1,4,5,7,6,5,4)
res=tuple1.count(4)
print('Count of 4 in tuple1 is: ',res)
res=tuple1.index(5)
print(res)
res=tuple1.index(5,3,10) # syntax: tuple.index(element,start,end)
print(res)
res=len(tuple1)
print(res)