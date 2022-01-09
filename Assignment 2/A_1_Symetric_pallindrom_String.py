# Write a python program to check whether the string is Symmetrical or Palindrome.
"""
A string that, when broken into two halves, produces two similar sequences of characters is called a symmetrical string. That is, the division occurs in the middle.
"""
string = (input("Enter String :"))
half = int(len(string) / 2)

if len(string) % 2 == 0: # even
	first_str = string[:half]
	second_str = string[half:]
else: # odd
	first_str = string[:half]
	second_str = string[half+1:]

# symmetric
if first_str == second_str:
	print(string, 'string is symmertical')
else:
	print(string, 'string is not symmertical')

# palindrome
if first_str == second_str[::-1]: 
	print(string, 'string is palindrome')
else:
	print(string, 'string is not palindrome')


"""
Enter String :aibohphobia
aibohphobia string is not symmertical
aibohphobia string is palindrome

Enter String :yoyo
yoyo string is symmertical
yoyo string is not palindrome

"""
