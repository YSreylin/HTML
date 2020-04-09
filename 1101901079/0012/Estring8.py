#write a Python function that takes a list of words and return the length of the longest one

a = input('Enter the senctence:')
b = a.split()
for i in b:
    y = max(b,key=len)
print('The length of the longest one is: ',y)



