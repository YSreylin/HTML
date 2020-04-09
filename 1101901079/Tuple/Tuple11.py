#write a Python program to convert list to tuple
Tuple = ()
list = []
a = int(input('Enter range for tuple:'))
for i in range(a):
    b = input("Enter the character for Tuple:")
    list.append(b)
print("The list is:",list)
c = tuple(list)
print("The Tuple is :",c)