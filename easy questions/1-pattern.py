symbol = input("e$nter the character to be printed")
n = int(input("enter the number of rows"))
if(n <= 0):
    print("number of rows cannot be negative")
for i in range(0, n):
    for j in range (0, i + 1):
        print(symbol, end = " ")
    print("\n")






        



