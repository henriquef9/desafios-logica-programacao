def maxSubArray(nums):
    
    current_sum = nums[0]
    best_sum = 0

    for num in nums:
        current_sum += num
        best_sum = max(best_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    
    return best_sum

