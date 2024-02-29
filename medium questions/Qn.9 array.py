arr={40,16,87,36,25,89,34}
array=sorted(arr)
print(array)
m=int(input("Enter the Mth Value :"))
n=int(input("Enter the Nth Value :"))
print(f"The {m} Maximum value :{array[len(array)-m]}")
print(f"The {n} Minimum value :{array[n-1]}")
