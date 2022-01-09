# 2. Write a python program Check if a Substring is Present in a Given String

string = input("Enter string:")
sub_str = input("Enter word:")
if string.find(sub_str) == -1:
    print("Substring not found in string!")
else:
    print("Substring found in string!")
