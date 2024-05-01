
# Match Case statements

x=int(input("Enter the value of x: "))
match x:
    case 0:
        print("X is zero.")
    case 4:
        print("case is 4.")
    case _: # this is default
        print(x)



# if case using 
x=int(input("Enter the value of x: "))
match x:
    case 0:
        print("X is zero.")
    case 4:
        print("case is 4.")
    case _ if x!=90: # Using if case in default
        print(x, "is not 90.")
    case _ if x!=80: 
        print(x, "is not 80.")
    case _: 
        print(x,)
