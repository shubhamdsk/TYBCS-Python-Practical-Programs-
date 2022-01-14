# 3. Write a Python program to print date, time for today and now.

import datetime

now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%d-%m-%Y %H:%M:%S"))
