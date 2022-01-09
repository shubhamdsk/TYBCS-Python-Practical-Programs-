# 3. Write a python program Words Frequency in String Shorthands

string = input("Enter String :")
print("\nEntered String :", string)

word = {key: string.count(key) for key in string.split()}

print("\nWords in the string :")
print(word)
