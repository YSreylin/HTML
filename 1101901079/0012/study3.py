#test1
def add():
    a=10
    b=20
    c=a+b
    return c
c=add()

print(c)

#test2 require parameter : the posting are in order
def student(name,rol):
    print("Enter your name:\n")

student("lin",20)


#test3 keyword parameter : the out put is played not in order or random
def student(name,roll,mark):
    print(name,roll,mark)
student(102,90,"lin")


#test4 defualt parameter : the value is asign to funtion defi so in no need to post value in funtion calling
def student(name,age=20):
    print(name,age)
student("lin")
student("meng")

#test5 vairiable length parameter
def student(name,*mark):
    print(name,mark)
student("lin,mey,meng",90,90,90)
