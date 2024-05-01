
# While loop

i=int(input("Enter the number: "))
while(i<5):
    print(i)
    i=i+1

print("Done with the loop.")


# decriment loop
count=5
while(count>0):
    print(count)
    count=count-1


# Else with while loop
count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("I am inside else.")



# do-while loops
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break