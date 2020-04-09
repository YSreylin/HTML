'''Write a Python program to get a string from two given number strings, separated by a space and swap
 the first two characters of each string'''
b = input('Enter the character:')
c = input('Enter the character:')

x = b[0:2]
y = c[0:2]

p = b.replace(x,y)
print(p)
q = c.replace(y,x)
print(q)
