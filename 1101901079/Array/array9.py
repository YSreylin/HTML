#write a python program to append items from a specified list
from array import *
list = []
a = eval(input('Enter range:'))
for i in range(a):
    b = eval(input('Enter number of list:'))
    list.append(b)
print('This is the list:',list)
array = array('i',[])
array.fromlist(list)
print(array)