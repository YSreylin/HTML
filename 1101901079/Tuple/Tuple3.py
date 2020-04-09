# #write a Python program to create one tuple with number and print one item
# list = []
# a = int(input("Enter the range for Tuple:"))
# for i in range(a):
#     b = eval(input("Enter many number:"))
#     list.append(b)
# c = tuple(list)
# print(c)
# print("Enter the location of one item to print:", input("Enter one item to print:"))

item = tuple(map(int,input('Item is:')))
print(item)



