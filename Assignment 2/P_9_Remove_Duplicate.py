# 9. Write a python program to Remove all duplicates from a given string in Python

"""
An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted.

The fromkeys() method returns a dictionary with the specified keys
"""

from collections import OrderedDict
def remove_duplicate(str):
  return "".join(OrderedDict.fromkeys(str))

str = input("Enter String : ")
print(remove_duplicate(str))

"""
Enter String : python program
python rgam

"""
