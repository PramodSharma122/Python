
# if-else statements

a=int(input("Enter your age: "))
print("Your age is :",a)

# conditional operators
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)

if(a>18):
    print("You can Drive: ")
else:
    print("You cannot Drive: ")



# elif statement
num=int(input("Enter the value of num: "))

if(num<0):
    print("Number is negative.")
elif(num==0):
    print("Number is zero.")
elif(num==99):
    print("Number is Special.")
else:
    print("Number is posative.")




# Nested if statement
num=int(input("Enter the value of num: "))

if(num<0):
    print("Number is negative.")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10.")
    elif(num>10 and num<=20):
        print("Number is between 11-20.")
    else:
        print("Number is greater than 20.")
else:
    print("Number is zero.")
