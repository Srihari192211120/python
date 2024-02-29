low=int(input("Enter the Starting Range :"))
high=int(input("Enter the Ending Range :"))
liist=[]
if(low>high or low<0 or high<0):
    print("Invalid Range")
else:
    liist=[(i,i**2) for i in range(low,high+1)]
print(tuplee)
