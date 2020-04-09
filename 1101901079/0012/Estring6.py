'''write a Python program to add 'ing' at the end of a given string (length should be at least 3).
 If the given string already ends with 'ing' then add 'ly' instead.
 if the string lenth of the given string is less then 3, leave it unchanged'''

a = input("Enter the word:")
x = a[-3:]
if len(a)>3:
    if x=='ing':
        print(a+"ly")
    else:
        print(a+"ing")
else:
    print(a)



