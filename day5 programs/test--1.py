def findSum(num):
    sum = 0
    while(num!=0):
        rem = num%10
        sum+= rem
        num//=10
    return sum

num = int(input("enter a number to find the sum of its digit: "))
print(findSum(num))

