# 4.Write python program to check Prime Number between range

start = int(input("Enter start Number:"))
end = int(input("Enter end Number:"))

for n in range(start, end + 1):
    flag = 0
    for i in range(2, n):
        if (n % i) == 0:
            flag = 1
            break
    if flag == 0:
        print(n)
