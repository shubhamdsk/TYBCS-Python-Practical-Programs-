# 1) Write a Python program to sum all the items in a list.

total = 0

list = [17, 9, 00, 9, 17]

for item in range(0, len(list)):
	total = total + list[item]

print("Sum of all elements in given list:",total)
