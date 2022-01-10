# 10. Write a Python function that checks whether a passed string is palindrome or not.

def isPalindrome(string):
	return string == string[::-1]

string = input("Enter String : ")
Palindrome = isPalindrome(string)

if Palindrome:
	print("String is Palindrome")
else:
	print("String is not Palindrome")

"""
Enter String : nayan
String is Palindrome

Enter String : python
String is not palindrome
"""



