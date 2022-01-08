# Maximum Number

x = int(input("Enter 1st Number:"))
y = int(input("Enter 2nd Number:"))
z = int(input("Enter 3rd Number:"))

if (x > y) and (x > z):

    print("Largest number", x)
    
elif (y > x) and (y > z):

    print("Largest number", y)
else:

    print("Largest number", z)
