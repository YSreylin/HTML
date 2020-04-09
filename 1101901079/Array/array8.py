#write a python to convert an array to an array of machines values and return the bytes repsentation
from array import *
import binascii
print("Bytes to String ")
x = array('b', [])
a = eval(input('Enter range :'))
for i in range(a):
    b=eval(input('Enter number :'))
    x.append(b)
s = x.tobytes()
print(s)
print(binascii.hexlify(s))