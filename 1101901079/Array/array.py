#write python program to create an array of 5 integers and display the array items.
#access individual element through indexes.
import array
a=array.array('i',[])
for i in range(5):
    c=int(input("Enter array:"))
    a.append(c)
print(a)


