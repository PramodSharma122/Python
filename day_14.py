
# Break and continue statement

# Break
for i in range(12):
    print(i)
    if(i==5):
        break
    else:
        print("Mississippi")
print("Thank you")



# Continue statement
for i in range(12):
    if(i==10):
        print("Skip the iteration.")
        continue
    print("5 x", i,"=", 5*i)
