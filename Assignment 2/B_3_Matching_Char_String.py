# 3. Write a python program to Count the Number of matching characters in a pair of string
def count(s1, s2):
    c = 0  # counter variable
    j = 0
    for i in s1:
        if s2.find(i) > -0 and j == s1.find(i):
            c = c + 1
        j = j + 1
    print("Matching char: ", c)

s1 = input("Enter the string1 : ")
s2 = input("Enter the string2 : ")
count(s1, s2)
