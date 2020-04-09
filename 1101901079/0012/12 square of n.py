#this program was written to show the table of square n
x = int(input("Enter x : "))
y = int(input("Enter y : "))
for i in range(1,y+1):
    c = x*(i**2)
    print(x,"x",i,"^2  =",c)
