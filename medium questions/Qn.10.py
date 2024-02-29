def comm(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
def prim(num):
    s=0
    for i in range(1,num):
        if(num%i==0):
            s=s+i
    if(s==num):
        return True
    else:
        return False
arr=input("Enter the numbers :")
array=arr.split()
array2=[int(num) for num in array]
com=[]
prime=[]
for i in array2:
    if(comm(i)==True):
        com.append(i)
for i in array2:
    if(prim(i)==True):
        prime.append(i)
print("Prime Numbers :",len(com))
print("Composite Numbers :",len(prime))
