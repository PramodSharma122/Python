
# Write a program to pronounce list of names using win32 API> If you are given a list L as follows.
# Your program should pronounce
# Shoutout to Prem
# Shoutout to Pramod


# for mac
from os import system
names=["prem","pramod"]
for name in names:
    system(f"say Shoutout to {name}")