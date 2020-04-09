#write python to reverse the order of item to array
import array
a=array.array('i',[])
b = int(input('Enter the range:'))
for i in range(b):
  c=int(input("Enter number:"))
  a.append(c)
print('Array is :',a)
print('Reverse array is:',a[::-1])

