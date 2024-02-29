p=int(input("Enter P Value :"))
q=int(input("Enter Q Value :"))
r=int(input("Enter R Value :"))
if(p>q or p==q and q==r):
    print("Inavlid")
else:
    for i in range(p,q+1):
        if str(r) not in str(i):
            print(i)
