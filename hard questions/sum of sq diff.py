limit = int(input("enter the limit: "))
sum1 = 0
sum2 = 0
for i in range(1,limit+1):
    sum1 += i**2
    sum2+=i
sqofsum=sum2**2
print(sum1)
print(sqofsum)

print("difference: ",sqofsum - sum1)





