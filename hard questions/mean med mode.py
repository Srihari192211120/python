length = int(input("enter the num of charecters: "))  
array = []
for i in range(length):
        temp = int(input("enter the array element: "))
        array.append(temp)

#mean
sumof = sum(array)
mean = sumof//length

#median
if(length % 2 == 0):
    median1 = array[length//2-1]
    median2 = array[length//2]
median = (median1 + median2)/2

#mode
unique = []
modeval = []
for i in array:
    if (i not in unique):
        unique.append(i)
    else:
        modeval.append(i)


print("mean: ", mean)
print("median: ", median)
print("mode: ", modeval)


