def sumF(num):
    sum = 0
    while num!=0:
        digit = int(num%10)
        sum += digit
        num = num/10
    return sum


num = int(input("enter a number"))
print(sumF(num))

