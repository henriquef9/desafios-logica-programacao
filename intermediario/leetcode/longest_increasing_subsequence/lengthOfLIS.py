
def LISWithStartingIndex(nums, index, memo):
    maxSize = 1
    
    if memo[index] >= 0:
        return memo[index]
    
    for i in range(index+1, len(nums)):
        if nums[i] > nums[index]:
            size = 1 + LISWithStartingIndex(nums, i, memo)
            maxSize = max(maxSize, size)
            memo[i] = size - 1
    return maxSize
        

def lengthOfLIS(nums):
    
    maxSize = 0
    memo = [-1]*len(nums)
    
    for i in range(len(nums)):
        size = LISWithStartingIndex(nums, i, memo)
        maxSize = max(maxSize, size)
    
    return maxSize
    