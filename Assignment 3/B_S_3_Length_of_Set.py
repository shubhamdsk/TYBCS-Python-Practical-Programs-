# 3. Write a Python program to find the length of a set.

setn = {5, 10, 3, 15, 2, 20}
print("\nOriginal set elements:")
print(setn)
print(type(setn))
print("Length of the set:")
print(len(setn))

setn = {5, 5, 5, 5, 5, 5}
print("\nOriginal set elements:")
print(setn)
print("Length of the set:")
print(len(setn))

setn = {5, 5, 5, 5, 5, 5, 7}
print("\nOriginal set elements:")
print(setn)
print("Length of the set:")
print(len(setn))


"""
Original set elements:
{2, 3, 20, 5, 10, 15}
<class 'set'>
Length of the set:
6

Original set elements:
{5}
Length of the set:
1

Original set elements:
{5, 7}
Length of the set:
2
"""