# Write a Python program to reverse a string.
def reverse_string(str):  
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1    # It will return the reverse string to the caller function  
     
string = input('Enter String : ')    

print("The original string is : \n",string)  
print("The reverse string is : ",reverse_string(string)) # Function cal