#write a python program to find the index of a tuple
Tuple = ()
list = []
a = int(input('Enter range for tuple:'))
for i in range(a):
    b = input("Enter the character for Tuple:")
    list.append(b)
c = tuple(list)
print("The Tuple is :",c)

d = int(input("Enter index:"))
print(c[d])