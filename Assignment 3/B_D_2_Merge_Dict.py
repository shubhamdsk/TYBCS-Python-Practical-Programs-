# 2. Write a Python script to merge two Python dictionaries.

d1 = {'a': 100, 'b': 200}
print("Dictionary 1:",d1)
d2 = {'x': 300, 'y': 200}
print("\nDictionary 2:",d2)
d = d1.copy()
d.update(d2)
print("\nMerged Dictionary :\n",d)

"""
Dictionary 1: {'a': 100, 'b': 200}

Dictionary 2: {'x': 300, 'y': 200}

Merged Dictionary :
 {'a': 100, 'b': 200, 'x': 300, 'y': 200}
"""
