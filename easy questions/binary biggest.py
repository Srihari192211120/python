def largestBinaryNum(bin1,bin2,bin3):
    bin1_dec = int(bin1, 2)
    bin2_dec = int(bin2, 2)
    bin3_dec = int(bin3, 2)
    max_dec = max(bin1_dec, bin2_dec, bin3_dec)
    max_bin = bin(max_dec)[2:]

    return max_bin
    
    
bin1 = input("enter the first bin number: ")
bin2 = input("enter the second bin number: ")
bin3 = input("enter the third bin number: ")

print("the maximum element is : ")
print(largestBinaryNum(bin1,bin2,bin3))

    
    
    
