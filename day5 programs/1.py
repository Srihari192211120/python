def func(limit):
    my_list = []
    for i in range(1,limit+1):
       if (i%3 == 0 and i%5 == 0):
           my_list.append('FizzBuzz')
       elif(i%3 == 0):
           my_list.append('Fizz')
       elif(i%5 == 0):
           my_list.append('Buzz')
       else:
           my_list.append(str(i))
           
    return my_list
        
           
n = int(input("enter the range: "))
print(func(n))
