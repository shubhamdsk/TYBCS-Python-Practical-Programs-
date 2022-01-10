# 2) Write a Python program to multiplies all the items in a list.

def mult_list(list):

    product = 1
    for i in list:
        product = product * i
    return product

list1 = [17, 9, 8, 1]
print(list1)
print("product: ", mult_list(list1))
