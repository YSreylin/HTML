#write a Python program to count the occurrences of each word in a given sentence.

a = input('Enter the sentence:')
y = a.split()
print(y)
for i in set(y):
    print(i+':',(a.count(i)),)

