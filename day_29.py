
# Exception Handling in python
# Error handling


a=input("Enter the number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:
    print("Invalid Input!")

print("End of program.")

try:
    num=int(input("Enter an number: "))
except ValueError:
    print("Number entered is not an integer.")


# Multiple Except
try:
    num=int(input("Enter an number: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error.")