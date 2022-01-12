# 3) Write a Python program to create set difference.

set1 = set([1, 1, 2, 3, 4, 5])
set2 = set([1, 5, 6, 7, 8, 9])

print("\nOriginal sets:")
print(set1)
print(set2)

r1 = set1.difference(set2)
print("\nDifference of set1 - set2:")
print(r1)

r2 = set2.difference(set1)
print("\nDifference of set2 - set1:")
print(r2)

"""

Original sets:
{1, 2, 3, 4, 5}
{1, 5, 6, 7, 8, 9}

Difference of set1 - set2:
{2, 3, 4}

Difference of set2 - set1:
{8, 9, 6, 7}
"""