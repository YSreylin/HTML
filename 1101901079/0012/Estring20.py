''' write a Python function to reverse a string if it's length is a multiple of 4'''
a = input('Enter the string :')
if len(a)%4==0:
    print(''.join(reversed(a)))
else:
    print(a)
