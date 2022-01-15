# 3) Write a python program to Check if String Contain Only Defined Characters using Regex
import re
def check(str, pattern):
	
	if re.search(pattern, str):
		print("Valid String")
	else:
		print("Invalid String")

pattern = re.compile('^[179]+$')
check('179', pattern)
check('123', pattern)
