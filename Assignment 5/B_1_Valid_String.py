"""
1) Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.Write a Python program to raised the attribute error, if attribute class object has no attribute with the name attribute
"""
import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_is_1_Programming_language"))
