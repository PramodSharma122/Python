
# os module in python:

import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")
    



# folder rename
for i in range(0,100):
    os.rename(f"data/Day{i+1}",f"data/Tutorial {i+1}")





# showing folder in oslist
import os
folders=os.listdir("data")
print(folders)

for folder in folders:
    print(folder) # print folder name in line by line
    print(os.listdir(f"data/{folder}")) # check the folder and which folder are present inside the main folder.
    


# showing the working directory and change.
    
print(os.getcwd())
os.chdir("/Users") # change the directory.
print(os.getcwd()) # print the working directory.