# 2. Write a Python program to compute the no of char, words and lines in a file.

file = open("A_2_Test.txt","r")

no_of_lines = 0
no_of_words = 0
no_of_char = 0

for line in file:
    line = line.strip("\n")   
    words = line.split()

    no_of_lines += 1
    no_of_words += len(words)
    no_of_char += len(line)

file.close()
print("lines:", no_of_lines, "words:", no_of_words, "char:", no_of_char)
