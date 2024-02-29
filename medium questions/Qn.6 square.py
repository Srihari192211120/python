 def summ(num):
    s=0
    while(num!=0):
        d=num%10
        s=s+d
        num=num//10
    return s
def sqrtt(num):
    sqrt=int(num**0.5)
    temp=sqrt*sqrt
    if(temp==num):
        return True
    else:
        return False
low=int(input("Enter the Starting Range :"))
high=int(input("Enter the Ending Range :"))
tuplee=[]
if(low>high or low<0 or high<0):
    print("Invalid Range")
else:
    for i in range(low,high+1):
        if(summ(i)<10 and sqrtt(i)):
            tuplee.append(i)
print("Tuple :",tuplee)
