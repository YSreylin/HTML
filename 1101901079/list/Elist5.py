'''Write a Python program to count the number of string where the strong length is 2 or more and the first
and last character are same from a given list of string.'''


b = input('Enter the string:')
c = b.split()
print(c)
d = 0
for i in c:
    if len(i)>2 and i[0]==i[-1]:
        d += 1
print(d)

