# 2) Write a python program to Reverse words in a given String

string = (input("Enter String :"))

words = string.split()

words = list(reversed(words))

print(" ".join(words))

"""
Enter String :hello python
python hello
"""
