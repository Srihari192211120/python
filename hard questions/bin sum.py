bin1 = input("binary 1:")
bin2 = input("binary 2:")
len1 = len(bin1)
len2 = len(bin2)

if(bin1[0] == '0' and len1 != 1):
    bin1 = bin1.lstrip('0')
if(bin2[0] == '0' and len2 != 1):
    bin2 = bin1.lstrip('0')

dec1 = int(bin1, 2)
dec2 = int(bin2, 2)

sumofdec = (dec1 + dec2)
modBin = bin(sumofdec)[2:]
print(modBin)



