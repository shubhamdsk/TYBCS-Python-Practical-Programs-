# 11. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

words=[n for n in input("Enter Words separated by hypen(-):").split('-')]
words.sort()
print("The Words in a hyphen-separated sequence after Sorting : ",'-'.join(words))

"""
Enter Words separated by hypen(-):python-java-php-perl-html-css
The Words in a hyphen-separated sequence after Sorting :  css-html-java-perl-php-python
"""