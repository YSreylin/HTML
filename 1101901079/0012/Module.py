print("hi\nhello")
print("hi\\hello")
print("'")
print("\"")
print("hi\thello")
print("\a")

#test
import array
sum=0
a=array.array('i',[1,2,3,4])
for i in a:
    sum=sum+i
print(sum)

#test1
import array
sum=0
l=[6,7,8,9,5]
a=array.array('i',[])
a.fromlist(l)
for i in a:
    sum=sum+i
print(sum)