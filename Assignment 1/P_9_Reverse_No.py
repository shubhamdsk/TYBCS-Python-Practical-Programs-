# 8.Write python program to print Reverse Number

n = int(input("Enter Number:"))
rev = 0

while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10

print("Reverse of number is:", rev)
