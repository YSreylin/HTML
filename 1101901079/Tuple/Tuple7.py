#Write a Python program to get the 4th element and 4 element from last of the Tuple
Tuple = ()
list = []
a = int(input('Enter range for tuple:'))
for i in range(a):
    b = input("Enter the character for Tuple:")
    list.append(b)
c = tuple(list)
print("The Tuple is :",c)
la = c[3]
print("\n The 4th element of Tuple is:",la)
print(" The 4th element of Tuple from last of Tuple is:",c[-4])