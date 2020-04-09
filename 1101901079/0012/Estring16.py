''' write a Python program to insert a string in the middle of a string'''

a = input("Enter the input of a:")
y = a.split()
b = input('Enter the input in the middle of a:')
x = len(y)//2
y.insert(x,b)
print(y)
print(" ".join(c for c in y))







