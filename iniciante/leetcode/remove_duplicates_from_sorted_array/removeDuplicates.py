
def removeDuplicates(nums):
    
    l = 0
    r = 0

    while r < len(nums):

        if nums[l] != nums[r]:
            l+=1
            nums[l] = nums[r]
        
        r+=1

    return l+1, nums




print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))