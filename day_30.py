
# Finally keyword in python.

# Difference between finally.

try:
    l=[1,2,5,6,7]
    i=int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred.")
finally:
    print("I am always executed.")
# print("I am always executed.") # In this case return this print in the result 



def func():
    try:
        l=[1,2,5,6,7]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred.")
        return 0
    finally:
        print("I am always executed.")
    # print("I am always executed.") # when i use def function then doesnot return this print in the result.
        
print(func())