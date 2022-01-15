# 1. Write a Python program to demonstrate the zero division error and overflow error.
import math

data = 50
try:
    data = data / 0  # data = data / 5
except ZeroDivisionError:
    print("Zero Division Error")
else:
    print("Division successful :", data) #Division successful : 10

try:
    a = math.exp(1000) #math.exp(2)
    print(a) #7.38905609893065
    """
The math. exp() method returns e raised to the power of x (Ex). 'e' is the base of the natural system of logarithms (approximately 2.718282) and x is the number passed to it.
    """
except OverflowError:
    print("Overflow Error")
