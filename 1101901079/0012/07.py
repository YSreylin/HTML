#this program is used to find the largest among of three number
a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
c = int(input("Enter your third number:"))

if a>b and a>c:
    print("First is the largest number")
elif b>a and b>c:
    print("Second is the largest number")
else:
    print("Third is the largest number")