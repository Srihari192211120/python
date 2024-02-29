from itertools import permutations
per=[]
str1=input("enter string :")
perm=permutations(str1)
for p in perm:
    if p not in per:
        per.append(p)
print(per)
