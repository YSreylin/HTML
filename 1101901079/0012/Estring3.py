'''write Python program to get a string made of the first 2 and the last chars from a given a string
if the string length is less than 2, return instead of the empty string'''

a = input('Enter the words:')
if len(a)>2:
    print(a[:2]+a[-2:])
else:
    print('empty string')


