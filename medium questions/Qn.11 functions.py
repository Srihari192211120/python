import math
def switch(x,n,ch):
    if(ch==0):
        print("Pow(x,n) =",math.pow(x,n))
    elif(ch==1):
        print("Add(x,n) =",x+n)
    elif(ch==2):
        print("Sub(x,n) =",x-n)
    elif(ch==3):
        print("Mul(x,n) =",x*n)
    elif(ch==4):
        print("Div(x,n) =",x/n)
    else:
        print("Invalid Choice....")
        
x=int(input("Enter X value :"))
n=int(input("Enter N value :"))
ch=int(input("Enter the choice :"))
switch(x,n,ch)
