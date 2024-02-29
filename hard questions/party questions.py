E = []
L = []
t = int(input("enter num of houts: "))
entry = 0
leave = 0
res = []
for i in range(0, t):
    entering = int(input("enter number of entering at hour: "))
    E.append(entering)
for i in range(0, t):
    exiting = int(input("enter number of exiting at hour: "))
    L.append(exiting)

for i in range(t):
    entry+=E[i]
    leave+=L[i]
    current = entry-leave
    res.append(current)

maxGuestCount = max(res)
print("maximum guests: ", maxGuestCount)

