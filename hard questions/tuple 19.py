lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

result = [(num, num**2) for num in range(lower, upper+1)]

print("Sample Output:")
print(result)
