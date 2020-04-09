#write a Python progrram to count the number of characters(character frequecy) in a string
a = input('Enter your strings:')
count={}
for i in a:
    if i in count.keys():
        count[i]+=1
    else:
        count[i] =1
print(count)


