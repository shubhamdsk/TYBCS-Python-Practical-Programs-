# Write a python program to check whether the string is Symmetrical or Palindrome.
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
if first_str == second_str[::-1]: # ''.join(reversed(second_str)) [slower]
	print(string, 'string is palindrome')
else:
	print(string, 'string is not palindrome')
