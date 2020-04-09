#write a python program to multiplies all the items in a list
a=[]
b=int(input('Enter the range for list: '))
for i in range(b):
    c= int(input('Enter the value for list:'))
    a.append(c)
print(a)
mul=1
for j in a:
    mul=mul*j
print('The result of multiplies of list is:',mul)