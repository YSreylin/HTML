#write a Python program to get the largest number from a list
a=[]
b=int(input('Enter the range of list:'))
for i in range(b):
    c=int(input('Enter the value in list:'))
    a.append(c)
print('The largest number is:', max(a))