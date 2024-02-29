def my_fun(x):
    if x <= 0:
        return 1
    return x*my_fun(x-1)

x=int(input())
print(my_fun(x))
      
