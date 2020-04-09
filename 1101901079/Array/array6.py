#write a python program to get the number of accurrences of a specified element in an array
from array import *
num = array('i', [])
a = eval(input("Enter the range:"))
for i in range(a):
    b = eval(input('Enter the number:'))
    num.append(b)
print("Original array: ",(num))
c = eval(input('Enter the number you want to count:'))
print("Number of occurrences of the number 3 in the said array: ",(num.count(c)))
