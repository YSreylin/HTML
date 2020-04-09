#write a python to remove a specified items using the index from an array
import array
array = array.array('i',[1,3,4,5,6,7])
print("The original array are:", array)
a = int(input("Enter the place number you want to delete:"))
array.pop(a)
print(array)
