#write a python to insert a new items before the second element in an existing array
from array import*
num = array('i',[])
a = eval(input('Enter the range:'))
for i in range(a):
    b = eval(input('Enter the number of array:'))
    num.append(b)
print('Original array is :',num)
a = int(input('insert new value before second element:'))
num.insert(1,a)
print("New array are: ",num)
