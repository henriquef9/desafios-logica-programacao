def sortColors(nums):
    
    l = 0
    r = len(nums) - 1

    while l < r:

        if nums[l] != 2:
            l+=1

        if nums[r] != 0:
            r-=1
        
        if nums[l] == 2 and nums[r] == 0:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
    
    l = 0
    r = len(nums) - 1

    while l < r:

        if nums[l] != 2:
            l+=1

        if nums[r] != 1:
            r-=1
        
        if nums[l] == 2 and nums[r] == 1:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1        
    
    return nums
        
        
nums = [2,0,2,1,1,0]

print(sortColors(nums))