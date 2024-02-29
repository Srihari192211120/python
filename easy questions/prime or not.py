num = int(input("enter a number: "))

flag = False
if(num <= 1):
    print("the given number is not a prime number")
else:
    for i in range(2, num):
        if(num % i==0):
            flag = True
            break
if(flag == True):
    print("the given number is noy prime")
else:
    print("prime number")
    
    
