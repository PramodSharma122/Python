
# Snake Water Gun

# Write a python program to create a snake water Gun game in python using if-else statements.Do not create any fancy GUI.Use proper functions to check for win.


import random
def check(comp,user):
    if comp==user:
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==2 and user==0):
        return -1
    if(comp==1 and user==2):
        return -1
    
    return 1
comp=random.randint(0,2)
user=int(input("0 for Snake, 1 for Water and 2 for Gun: "))

score=check(comp,user)
print("You: ",user)
print("Computer: ",comp)

if(score==0):
    print("It's a draw")
elif (score==-1):
    print("You Lose")
else:
    print("You Won")