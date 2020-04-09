#this program is written for calculate x to the power of y
x = int(input("Enter your number : "))
y = int(input("Enter your exponential : "))

p = 1
for i in range(1,y+1):

    p = p*x

print(p)

