#write a Python program to find the repeated item of tuple
Tuple = ()
list = []
a = int(input('Enter range for tuple:'))
for i in range(a):
    b = input("Enter the character for Tuple:")
    list.append(b)
c = tuple(list)
print("The Tuple is :",c)
b = input("Enter number you want to count:")
con = c.count(b)
print(con)