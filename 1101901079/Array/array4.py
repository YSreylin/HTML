"""write python program to get the length in bytes
of one array item in the internal representation"""
from array import*
b = array('u',[])
c = input("enter value:")
b.append(c)
print(b.itemsize)
