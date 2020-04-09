''' write a Python program to get a string made of its first three character of a specified string.
if the length of the string is less than 3 then return the original string'''

a = input('Enter the string:')
if (len(a)>3):
    print(a[:3])
else:
    print(a)