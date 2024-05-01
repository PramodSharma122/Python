
# Write a python program to translate a message into secret code language.Use the rules below to translate normal English into secret code language.
import random

st=input("Enter the Message: ")
words=st.split(" ")
coding=input("'1' for Coding or '0' for Decoding: ")
coding=True if (coding=="1") else False
def generate_random_string(length=3):
    return ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length))


if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1=generate_random_string()
            r2=generate_random_string()
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))