# 2. Write a Python program to print each line of a file in reverse order.

f1 = open("B_2_output.txt", "w")

with open("B_2_Test.txt", "r") as myfile:
	data = myfile.read()
data_1 = data[::-1]
f1.write(data_1)
f1.close()
