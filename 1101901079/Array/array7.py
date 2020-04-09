#write a Python program to append items from inerrable to the end of array
from array import *
a = array('i', [1, 3, 5, 7, 9])
print("Original array: ",a)
b = eval(input('Enter the number you want to append at the end of array:'))
a.append(b)
print("New array: ",a)