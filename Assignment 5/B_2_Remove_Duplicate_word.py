# 2. Write a python Program to Remove duplicate words from Sentence

string = "Python is good Python is for beginners beginners"
 
print(' '.join(dict.fromkeys(string.split())))