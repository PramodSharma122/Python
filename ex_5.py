
# Q. Write a program to print the fibonacci sequence.
# f0=0
# f1=1
# f2=f1+f0
# fn=f(n-1)+f(n-2)

n = 10
num1 = 0
num2 = 1
next_number = num1
count = 1

while count <= n:
	print(next_number,end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()
