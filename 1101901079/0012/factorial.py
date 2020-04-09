#find the factorial of a number
def factoria(n):
    num = 1
    for i in range(1,n+1):
        num = num*i
    return num

a = int(input("Enter your value:"))
total = factoria(a)
print("Total is:",total)
