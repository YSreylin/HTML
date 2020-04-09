'''write a Python program ro find the first appearance of the substring 'not' and 'poor
from a given string. if 'not' follows the 'poor', replace the whole 'not' ...'poor' substring with
'good'. return the resulting string'''
a = input("Enter the sentence:")
if "not" in a and 'poor' in a :
    start = a.index("not")
    end = a.index("poor")

    if start < end:
        print(a[:start] + "good " + a[end + 4:])
    else:
        print(a)
else:
    print(a)
