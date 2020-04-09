#write a Python program to unzip a list of tuple into individual lists
list_of_tuples = [(1,2,3),(4,5,6),(7,8,9)]
print("List of Tuple is:",list_of_tuples)

individual_list = [list(i) for i in list_of_tuples]
print('individual list created: ', *individual_list)






#the following still creates a list of tuples
#print('still creates a list of tuples: ', list(zip(*list_of_tuples)))
