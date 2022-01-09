# 2. Write a python program to accept the strings which contains all vowels

myStr = input("Enter the string : ")

# Checking if the string contains all vowels or not
myStr = myStr.lower()
allVowels = set("aeiou")

for char in myStr:
    if char in allVowels:
        allVowels.remove(char)

print("Entered String is ", myStr)
if len(allVowels) == 0:
    print("Accepted \n")
else:
    print("Not Accepted \nThe string does not contain all vowels")

"""
Enter the string : aeiouAEIOU
Entered String is  aeiouaeiou
Accepted

Enter the string : aeibd
Entered String is  aeibd
Not Accepted
The string does not contain all vowels
"""
