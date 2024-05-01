
# File IO in python:


# Reading File
f=open('myfile.txt','r')

text=f.read()
print(text)
f.close()


# Writing a file
f=open('myfile2.txt','w')
f.write("Hello,world!")
f.close()


# The 'with' statement:
with open('myfile.txt','a') as f:
    f.write("Hey I am inside with")