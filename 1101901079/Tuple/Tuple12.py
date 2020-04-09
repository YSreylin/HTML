#Write a Python program to remove one item form tuple
Tuple = ()
list = []
a = int(input('Enter range for tuple:'))
for i in range(a):
    b = input("Enter the character for Tuple:")
    list.append(b)
c = tuple(list)
print("The Tuple is :",c)
b = input("Choose one item to remove:")
list.remove(b)
print(tuple(list))
