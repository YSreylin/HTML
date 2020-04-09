'''Write a Python program to get string from a given string where all occurrences
of its first clear have been changed to $, except the first char itself'''

a = input('Enter the string : ')
b = a[0]
c = a.replace(b,'$')
print(b + c[1:])
