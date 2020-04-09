#write a python program to slide the Tuple
Tuple = ()
list = []
a = int(input('Enter range for tuple:'))
for i in range(a):
    b = input("Enter the character for Tuple:")
    list.append(b)
c = tuple(list)
print("The Tuple is :",c)

d = int(input("Enter the start number to slice:"))
e = int(input("Enter the end number to slice:"))
print(c[d:e])
