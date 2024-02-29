inputString = input('enter a string: ') 
inputChar = "A"
splitted = inputString.split()
counts = 0
for elements in splitted:
    if('A' in elements):
        counts+= 1

print(counts)
