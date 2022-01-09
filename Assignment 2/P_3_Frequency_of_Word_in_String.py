# 3. Write a python program Words Frequency in String Shorthands

string = input("Enter String :")
print("\nEntered String :", string)

word = {key: string.count(key) for key in string.split()}

print("\nWords in the string :")
print(word)

"""
Enter String :python is programming lang and java also programming lang

Entered String : python is programming lang and java also programming lang

Words in the string :
{'python': 1, 'is': 1, 'programming': 2, 'lang': 2, 'and': 1, 'java': 1, 'also': 1}

"""
