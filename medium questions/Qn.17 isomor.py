str1=input("Enter the First String :")
str2=input("Enter the second string :")
flag=0
mapp={}
if(len(str1)!=len(str2)):
    print("Not Isomorphic")
else:
    for i in range(len(str1)):
        if str1[i] not in mapp:
            mapp[str1[i]]=str2[i]
        elif(mapp[str1[i]]!=str2[i]):
            flag=1
print(mapp)
if(flag==0):
    print("Isomorphic")
else:
    print("Not")
    
