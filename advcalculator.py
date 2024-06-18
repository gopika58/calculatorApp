import math
def addition():

    a=int(input())
    b=int(input())
    print('sum',a+b)
def subtraction():
    n1=int(input())
    n2=int(input())
    print('difference',a-b)
def product():
    a=int(input())
    b=int(input())
    print('product',a*b)
def division():
    d1=int(input())
    d2=int(input())
    if(d2==0):
        print("cannot divide")
    print('division',d1/d2)
def square():
    a=int(input())
    print(a**2)
def squareroot():
    a=int(input())
    print("squareroot",math.sqrt(a))
def cuberoot():
    a=int(input())
    print("cuberoot",a**3)
print("enter choice")
choice=input()
print("enter  number")
if (choice=='add'):
    addition()
elif(choice=='subtract'):
    subtraction()
elif(choice=='multiply'):
    product()
elif(choice=='divide'):
    division()
elif(choice=="square"):
    square()
elif(choice=="squareroot"):
    squareroot()
elif(choice=="cuberoot"):
    cuberoot()