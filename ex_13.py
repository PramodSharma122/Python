
# Drink water Reminder
# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operation system.



import os
import time

REPEAT_INTERVAL=10
while True:
    command="osascript -e \'say \"Hello World!\"\'; osascript -e \'display alert \"Hello World\"\'"
    os.system(command)
    time.sleep(REPEAT_INTERVAL)