#  3) Write a python script to print the current date in the following format Sun May 29 02:26:23 IST 2017

import time
ltime = time.localtime()
print(time.strftime("%a %b %d %H:%M:%S %Z %Y", ltime))
