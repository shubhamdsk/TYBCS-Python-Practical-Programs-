# 8. Write a Python program to detect the number of local variables declared in a function.

"""
__code__ The code object representing the compiled function body.
co_nlocals is the number of local variables used by the function (including arguments);
"""
def scope():
   a = 17
   b = 9
   c = 2000
   str = 'Python'

print("Number of local varibales available:",scope.__code__.co_nlocals)

"""
Number of local varibales available: 4
"""
