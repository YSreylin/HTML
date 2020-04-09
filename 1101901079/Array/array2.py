#write a python program to append a new item in the end of 9array
import array
a=array.array('i',[2,4,5,7,4])
print('Original array:',a)
b=int(input("Enter the number to be last in array:"))
a.append(b)
print(a)
