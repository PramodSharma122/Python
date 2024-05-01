
# Dictionaries in python

dic={
    344:"Pramod",
    56:"Aabu",
    76:"Unique"
}
print(dic[56])


# Accessing single value:
info={'name':'Pramod','age':22,'eligible':True}
print(info)
print(info['name']) # if i donot use get throw error.
print(info.get('name2')) # if i use get didnot throw error.

# Accessing multiple values:
info={'name':'Pramod','age':22,'eligible':True}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
    print(info[key])



# Accessing key-value pairs:
info={'name':'Pramod','age':22,'eligible':True}
print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

