
#create a list
a = [2,3,4,5,6,7,8,9,10]
print(a)
#indexing
b = int(input('Enter indexing value:'))
print('The result is:',a[b])
print(a[8])
print(a[-1])

#slicing
print(a[0:3])
print(a[0:])

#conconteation
b=[20,30]
print(a+b)

#Repetition
print(b*3)

#updating
print(a[2])
a[2]=100
print(a)

#membership
print(5 in a)

#comparison
c=[2,3,4]
print(a==b)
print(a!=b)

#slice
a=[9,8,7,6,5,4]
print(a[0:3])

print(a[:4])
print(a[1:])
print(a[:])
print(a[2:2])
print(a[0:6:2])
print(a[0:6:3])

'''#a.apppend(element)
a=[1,2,3,4,5]
b=int(input('Enter number to append:'))
a.append(b)
print(a)
#insert(index,element)
a.insert(0,0)
print(a)
#a.extend(c)
c=[6,7,8,9]
a.extend(c)
print(a)

#one more'''


