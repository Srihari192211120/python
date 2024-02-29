def mean(arr):
    return (sum(arr)/len(arr))
def median(arr):
    if(len(arr)%2==0):
        return(arr[(len(arr)-1)//2]+arr[len(arr)//2])
    else:
        return(arr[len(arr)//2])

num=[1,2,3,4,5,6]
print("Mean :",mean(num))
print("Median :",median(num))

