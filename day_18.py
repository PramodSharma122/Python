
# List Methods

l=[5,8,1,2,4,6]
print(l)
l.append(7) # adding number in list
print(l)

l.sort() # sorting ascending order
print(l)

l.sort(reverse=True) # sorting descinding order
print(l)

l=[7,5,8,9,1]
l.reverse() # Reversing the orginal list
print(l)

l=[5,2,1,3,7,1,5,8,4,5]
print(l.index(1)) # index location of 1 (index of the first occurrence of the list item)
print(l.count(5))

m=l.copy()
m[0]=0
print(l)
print(m)

l.insert(1,899) # item is added in index number 1
print(l)

m=[900,1000,1100] # this items added in 'l' list at last index
l.extend(m)
print(l)


# concatenating two lists: same as extend()
k=l+m
print(k)