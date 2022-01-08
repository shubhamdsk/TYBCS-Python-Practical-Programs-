# 3.Write a python program to check if a number is Prime Number or not.

num = int(input("Enter start Number:"))
flag = 0
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = 1
            break
if flag:
    print(num, "is not a number prime")

else:
    print(num, "is a prime number")
