# 3.Write a python program to check if year is a leap year or not

# To get year (integer input) from the user
year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, "is Leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is leap year")
else:
    print(year, "is not a leap year")
