#write a Python program to convert Tuple to THe String
list = []
a = int(input("Enter the range for tuple:"))
for i in range(a):
    b = input("Enter value:")
    list.append(b)
c = tuple(list)
print("Tuple is:",c)
string = ' '.join(c)
print("The value of string is: ",string)

