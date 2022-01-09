# 4. Write a python program Convert Snake case to Pascal case

test_str = input("Enter String :")

# printing original string
print("The original string is : " + test_str)

res = test_str.replace("_", " ").title().replace(" ", "")

print("The String after changing case : " + str(res))

"""
Enter String :hello_shubham
The original string is : hello_shubham
The String after changing case : HelloShubham
"""
