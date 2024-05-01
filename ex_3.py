import time

timestamp=time.strftime('%H:%M:%S')
print(timestamp)
name=input("Enter your name: ")
timestamp=int(time.strftime('%H'))
if(timestamp>=0 and timestamp<12):
    print("Good Morning",name)
elif(timestamp>12 and timestamp<17):
    print("Good Afternoon",name)
elif(timestamp>17 and timestamp<21):
    print("Good Evening",name)
else:
    print("Good Night",name)