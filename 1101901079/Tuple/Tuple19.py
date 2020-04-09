#write a Python program to convert a list of tuple into a dictionary
list = []
a = int(input("Enter range for tuple: "))
for i in range(a):
 tuple1 = tuple(map(int,input("Enter the tuple :")))
 print(tuple1)
 list.append(tuple1)
print("The list of Tuple is: ",list)

d = {j for j in list}
print("Dictionary is:",d)



