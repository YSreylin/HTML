#write a Python program to find the  list of words that are longer than n from a given list of words
a = []
b = int(input("Enter range for list:"))
for i in range(b):
    c = input("Enter the string:")
    a.append(c)
for j in a:
    d = max(a, key=len)
print("\n",d,"is the longest one")
