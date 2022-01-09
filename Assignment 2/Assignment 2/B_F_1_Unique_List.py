# 1. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print("Unique elements of the first list :",unique_list([1,2,3,2,3,4,4,5])) 
