#write a Python program to remove the n^th index character from a nonempty string

x =input("Enter the sring:")
n = int(input("Enter the index of the character to remove:"))
first = x[:n]
last = x[n+1:]#+1 in n is deleted 1 letter, if 2 delete 2 letters
a=first + last

print(a)

