s1 = input("enter the first sentence: ")
s2 = input("enter the second sentence: ")
str1 = s1.split()
str2 = s2.split()
str3 = []
for i in str1:
    for j in str2:
        if(i in j):
            str3.append(i)
print(str3)
print("first sentence after conversion: ")
for i in str1:
    if(i not in str3):
        print(i)
print("second sentence after conversion: ")
for i in str2:
    if(i not in str3):
        print(i)

