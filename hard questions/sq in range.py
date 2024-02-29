lower_limit =int(input("enter the lower limit: "))
upper_limit = int(input("enter the upper limit: "))

def sumof(n):
    sum = 0
    while n!= 0:
        rem = n%10
        sum +=rem
        n =n//10
    return sum

my_list = []
for i in range(lower_limit, upper_limit + 1):
    if((int(i**0.5)**2) == i and sumof(i)<10):
        my_list.append(i)

print(my_list)
        
