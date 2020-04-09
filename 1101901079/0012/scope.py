#test1
a=50
def add():
    b=20
    c=a+b
    return(c)
c=add()
print(c)

def sub():
    b=30
    c=a-b
    return(c)
c=sub()
print(c)
print(a)

#test11
a=50
def add():
    b=20
    c=a+b
    print(c)
def sub():
    b=30
    c=a-b
    print(c)
add()
sub()
print(a)

#test2
def add(a,b):
    c=a+b
    return c

def mul(c,d):
    e=c*d
    return e

c=add(10,20)
e=mul(c,30)
print(e)



#test3
def sum(a,b):
    sum=a+b
    return sum
def avg(sum):
    avg=sum/2
    return avg
a=eval(input("Enter a:"))
b=eval(input("Enter b:"))
sum = sum(a,b)
avg = avg(sum)
print("The avg is :",avg)

#test4 recursion
def fact(n):
    if(n==1):
        return n
    else:
        return n*fact(n-1)
n=eval(input("Enter no. to find face:"))
fact=fact(n)
print("Fact is ", fact)


