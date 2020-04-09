#write a python program to delete duplicate of the list.
a=[]
b= int(input("Enter range for list:"))
for i in range(b):
    c= eval(input("Enter the number:"))
    a.append(c)
print("Original list is:")
print("After delete duplicated number:", sorted(set(a)))
