def smallerNumber(nums):
    counts = [0] * 201
    result = [0] * len(nums)
    for num in nums:
        counts[num] += 1
        
    for i in range(1,200):
        counts[i] += counts[i -1]
        
    for i in range(len(nums) -1, -1, -1):
        result[i] = counts[nums[i]]
        counts[nums[i]] -= 1


    return result
print(smallerNumber([6,5,4,8]))
        
