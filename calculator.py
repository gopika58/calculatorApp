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
    print('division',d1/d2)
print("enter choice")
choice=input()
print("enter 2 numbers")
if (choice=='add'):
    addition()
elif(choice=='subtract'):
    subtraction()
elif(choice=='multiply'):
    product()
elif(choice=='divide'):
    division()
