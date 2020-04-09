#write a Python program to clone or copy the list
a = []
b = int(input("Enter the range:"))
for i in range(b):
    c = int(input('Enter the number:'))
    a.append(c)
print("Original list is:",a)
d = a
print("Clone list is:",d)