# 4.Write python program to check Armstrong Number

n = int(input("Enter Number:"))
num = n
sum = 0
while n > 0:
    rem = n % 10
    sum = sum + rem * rem * rem
    n = n // 10
if num == sum:
    print(num, "is an armstrong")
else:
    print(num, "is not an armstrong")
