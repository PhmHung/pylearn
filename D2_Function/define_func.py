import math

def myabs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Incorrect type')
    if x >=  0:
        return x
    else: 
        return -x

def ucln(a,b):
    x=myabs(a)
    y=myabs(b)
    while y!=0 :
        r = x%y
        x=y
        y=r
    return x 

n = myabs(-20)
print(n)

# m = myabs('-20')
# print(m)

num1 = int(input("Nhap so 1: "))
num2 = int(input("Nhap so 2: "))

print(ucln(num1,num2))