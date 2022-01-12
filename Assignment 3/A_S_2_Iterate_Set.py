# 2) Write a Python program to iterate over sets.
 
num_set = set([0, 1, 2, 3, 4, 5])
for n in num_set:
  print(n, end=' ')

print("\n\nCreating a set using string:")
char_set = set("Python")  

for val in char_set:
    print(val, end=' ')

"""
0 1 2 3 4 5

Creating a set using string:
t h o P y n

0 1 2 3 4 5

Creating a set using string:
h y P o t n
"""