
# Regular Expressions in Python.


import re

pattern =r"[A-Z]+as"
text="hhadshd was jdmfvdd dfbkfhsd Was djfuh was sd Das jfghfd"

# match= re.search(pattern,text)
# print(match)

matches=re.finditer(pattern,text)
for match in matches:
    print(match)
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])


