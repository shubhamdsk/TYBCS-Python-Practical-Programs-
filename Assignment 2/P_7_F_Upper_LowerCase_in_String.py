# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


def string_test(str):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in str:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print("Original String : ", str)
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])


str = input("Enter String to calculate the number of upper case letters and lower case letters : ")
string_test(str)

"""
Enter String to calculate the number of upper case letters and lower case letters : Python LanguAGE
Original String :  Python LanguAGE
No. of Upper case characters :  5
No. of Lower case Characters :  9
"""