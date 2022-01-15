# 3. Write a python to| Remove all characters except letters and numbers

import re 
my_string = "python123:, .@! abc" 
print ("The string is : ") 
print(my_string) 
result = re.sub('[\W_]+', '', my_string) 
print ("The String after Removal is :") 
print(result)