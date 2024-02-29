inc=int(input("Enter the Income :"))
if(inc<=150000):
    tax=0
elif(inc>150000 and inc<300000):
    tax=(10/100)*inc
elif(inc>300000 and inc<500000):
    tax=(20/100)*inc
elif(inc>500000):
    tax=(30/100)*inc
print(int(tax))
