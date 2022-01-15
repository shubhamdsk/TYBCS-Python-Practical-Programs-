# 2. Write a Python program to find sequences of lowercase letters joined with a underscore
"""
A regular expression (or re) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression
"""
import re
def match(text):
		
		pattern = '[A-Z]+[a-z]+$'

		if re.search(pattern, text):
				return('Yes')
		else:
				return('No')

print(match(input("Enter Text :")))
