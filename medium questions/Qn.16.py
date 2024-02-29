a=int(input("Enter the first number :"))
b=int(input("Enter the seconod number :"))
c=0
if(a<b):
    for i in range(1,a+1):
        if(a%i==0 and b%i==0):
            c+=1
            print(i)
elif(b<a):
    for i in range(1,b+1):
        if(a%i==0 and b%i==0):
            c+=1
            print(i)
print("Count :",c)
