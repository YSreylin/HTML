from array import *
num = array('i', [])
a = eval(input("Enter the range:"))
for i in range(a):
    b=eval(input('Enter a number:'))
    num.append(b)
print("Current memory address and the length in elements of the buffer: ",num.buffer_info())
print("The size of the memory buffer in bytes: ",(num.buffer_info()[1] * num.itemsize))
