# 1. Write a Python program to check if a set is a subset of another set.

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print("A is SubSet B :",A.issubset(B))

print("B is SubSet A :",B.issubset(A))

print("A is SubSet C :",A.issubset(C))

print("C is SubSet B :",C.issubset(B))


"""
A is SubSet B : True
B is SubSet A : False
A is SubSet C : False
C is SubSet B : True
"""