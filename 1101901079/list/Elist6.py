'''Write a Python program to get a list, sorted in increasing order by the last element in each
tuple from a given list if non-empty tuples'''

from operator import itemgetter
a = [(2,1),(2,4),(3,9),(2,3)]
print('Original list is: ',a,"\n")
print('The result is:',sorted(a, key=itemgetter(1)))



