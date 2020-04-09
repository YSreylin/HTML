'''write a python program to convert an array to an ordinary list with the same items'''
import array
array = array.array('i',[])
a = eval(input('Enter the range:'))
for i in range(a):
    b = eval(input('Enter the array:'))
    array.append(b)
print("Original array:",array)
print("Convert array to list:")
list = []
list = array.tolist()
print(list)
