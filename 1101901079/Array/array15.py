'''write a python program to find the first duplicate element in a
given array of integers.
return -1 if there are no such element'''
from array import*
a = array('i',[])
b = eval(input("Enter the range:"))
for u in range(b):
    c = eval(input("Enter the number:"))
    a.append(c)

for y in a:
    h = a.count(y)
    if h>1:
        print('The first duplicate is number:',y)
        break
else:
  print('-1')
  