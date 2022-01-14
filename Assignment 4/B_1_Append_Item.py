# 1. Write a Python program to append text to a file and display the text.

testfile = open("B_1_test.txt", "a")

testfile.write("Line Four\n")
testfile.close()

appended_file = open("B_1_test.txt", "r")
print(appended_file.read())
