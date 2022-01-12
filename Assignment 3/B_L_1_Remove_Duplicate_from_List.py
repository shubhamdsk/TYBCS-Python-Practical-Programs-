# 1. Write a Python program to remove duplicates from a list.

list1 = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
print("List Before removing duplicates :\n", list1)
list2 = [] #Temporary List

for i in list1:
    if i not in list2:
        list2.append(i)

list1 = list2

print("List After removing duplicates :\n", list1)

"""
List Before removing duplicates :
 [1, 2, 3, 1, 2, 4, 5, 4, 6, 2]
List After removing duplicates :
 [1, 2, 3, 4, 5, 6]
"""