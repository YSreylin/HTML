#write a Python program to create a tuple with different data type
list = []
a = int(input("Enter the range for tuple:"))
for i in range(a):
    c = input("ENter the string:")
    list.append(c)
item = tuple(map(int,input("Enter number for tuple:")))
print(tuple(list)+item)

