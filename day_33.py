
# Enumerate Function in python.


# Without Enumerate function.
marks=[12,45,65,87,23,98,90]

index=0
for mark in marks:
    print(mark)
    if(index == 5):
        print("Pramod, awesome!")
    index +=1

    

# Use Enumerate Function
marks=[12,45,65,87,23,98,90]

for index, mark in enumerate(marks):
    print(mark)
    if(index == 5):
        print("Pramod, awesome!")



# Changing the start index
for index, mark in enumerate(marks,start=1):
    print(mark)
    if(index == 5):
        print("Pramod, awesome!")