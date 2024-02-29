strr="a"
l,u,n=0,0,0
while(strr!="*"):
    strr=input("Enter any character :")
    if(len(strr)==1):
        if(strr.isupper()):
            u+=1
        elif(strr.islower()):
            l+=1
        elif(strr.isdigit()):
            n+=1
        else:
            continue
    else:
        print("Invalid...Enter single Character..")
print("Total Upper Case :",u)
print("Total Lower Case :",l)
print("Total Number :",n)
