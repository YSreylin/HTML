#write a Python to get the smallest number from list
a = []
b = int(input('Enter the range for list:'))
for i in range(b):
    c = int(input('Enter the value for list:'))
    a.append(c)
print('The smallest number of this list is:', min(a))