# 1) Write a Python program to read an entire text file.

def file_read(A_1_Test):
    txt = open(A_1_Test)
    print(txt.read())

file_read("A_1_Test.txt")
