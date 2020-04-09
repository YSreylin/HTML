#this program to solve the quadratic equation
import cmath
a = float(input("Enter your value a: "))
b = float(input("Enter your value b: "))
c = float(input("Enter your value c: "))

d = b**2 - 4*a*c

sol1 = (-b-cmath.sqrt(d))/2*a
sol2 = (-b+cmath.sqrt(d))/2*a
print("The first answer is:",sol1)
print("The second answer is:",sol2)


