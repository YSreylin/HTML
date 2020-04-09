#write a Python program to convert tuple to dictionary
Tuple = ()
list = []
a = int(input('Enter range for tuple:'))
for i in range(a):
    b = input("Enter the character for Tuple:")
    list.append(b)
c = tuple(list)
print("The Tuple is :",c)

td = {i for i in c}
print("Dictionary is:",td)