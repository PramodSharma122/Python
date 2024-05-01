
# Walrus Operators(:=) in Python


a=True
print(a:=False)


numbers=[6,4,7,2,9,3]

while(n:=len(numbers))>0:
    print(numbers.pop())


happy=True
print(happy)

print(happy:= True)


foods=list()
while True:
    food=input("What food do you like?: ")
    if food == "quit":
        break
    foods.appends(food)

# use walrus operator
foods=list()
while(food:=input("What food do you like?: "))!="quit":
    foods.append(food)