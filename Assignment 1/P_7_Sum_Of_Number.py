# 7.Write python Program to Find the Sum of Natural Numbers
num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    # use while loop to iterate un till zero
    while num > 0:
        sum += num
        num -= 1
    print("The sum is : ", sum)
