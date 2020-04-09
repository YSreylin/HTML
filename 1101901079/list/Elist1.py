#writre a Python program to sum all the items in a list
a=[]
b= eval(input('Enter your range in list:'))
for i in range(b):
    c= eval(input('Enter the number:'))
    a.append(c)
print(a)
print('The sum of list is:',sum(a))
