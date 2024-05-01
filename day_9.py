
# String Methods

a="Pramod"
b="SHARMA" # strings are immutable
c="Prem Chalise"
print(len(a))
print(a.upper())
print(b.lower())
print(a.strip("P")) # strip and rstrip are same but rstrip are removing back side character of string and strip are front side character of string
print(b.rstrip("S"))
print(a.replace("Pramod","Prem"))
print(c.split(" "))

d="introDuction oF pYtHon"
print(d.capitalize())
print(d.center(50))
print(d.count("o"))
print(d.endswith("!!"))
print(d.endswith("oF",10, 15))
print(d.find("oF"))
print(d.index("oF"))  # find and index are same but when result is not found find function returns -1 and index function returns error.

e="Welcometopython"
print(e.isalnum()) # A-Z,a-z,0-9 

f="Welcome00"
print(f.isalpha()) # Only need string not a number

print(a.islower())
print(b.isupper())

a1="Home\n"
print(a.isprintable())
print(a1.isprintable()) # \n isnot print so result is false

# using spacebar
j="         "
print(j.isspace())

str1="World Health Organization"
str2="To kill a Mocking bird"
print(str1.istitle())
print(str2.istitle())

str1="Python is a Language"
print(str1.startswith("Python"))

str1="PyThOn Is A lAnGuAgE"
print(str1.swapcase()) # upper case to lower and lower case to upper case of string

str1="Python is a Language"
print(str1.title())
