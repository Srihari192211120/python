def numOfStrings(n):
    return ((n+1)*(n+2)*(n+3)*(n+4)/24)

n = int(input("enter the limit: "))

if(n<=0):
    print("invalid length")
else:
    print("count:",numOfStrings(n))
