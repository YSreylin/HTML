''' Write a Python program that accepts a comma separated sequence of words as
input and print the unique words in sorted form(alphanumerically).
'''

a = input('Enter many color:')
a = a.split(',')
print(','.join(sorted(list(set(a)))))
