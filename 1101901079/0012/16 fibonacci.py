#this program is to fine Fibonacci
x = int(input("Enter any number :"))
a = 0
b = 1
for i in range(1,x+1):
    c = a + b
    b = a
    a = c

print(c)


