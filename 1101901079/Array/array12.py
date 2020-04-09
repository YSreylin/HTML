'''write a python program to remove the first occurrence of a specified element from an array'''
import array
array = array.array('i',[1,2,3,4,6,7,8,9,1])
print('Original array:',array)
a = int(input('Choose number:'))
array.remove(a)
print(array)

