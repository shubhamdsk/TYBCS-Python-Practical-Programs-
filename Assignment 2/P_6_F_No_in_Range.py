# 6. Write a Python function to check whether a number is in a given range.

def test_range(n):
    if n in range(0, 9):
        print(n, "is in the range")
    else:
        print("The number is outside the given range.")


test_range(1)
