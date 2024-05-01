
# For loops

name="Pramod"
for i in name:
    print(i)
    if(i=="m"):
        print("This is special!")
    

# For list
colors=["Red","Blue","Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)



# Range function

for k in range(7):
    print(k) # this code returns 0 to 6

for k in range(5):
    print(k+1) # this code returns 0 to 5

for k in range(1,8):
    print(k) # this code returns 1 to 7

for k in range(1,12,3): # last ko 3 number le number haru 3-3 ko gap ma print garxa  
    print(k)