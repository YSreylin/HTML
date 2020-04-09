''' write a Python function to get a string made of 4 copies of the last two characters of a specified string
(length must be at least 2)'''

a = input('Enter the string:')
for i in range(4):
    b = a[-2:]
    print(b, end='')