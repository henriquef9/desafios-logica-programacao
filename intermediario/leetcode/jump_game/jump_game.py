
def canJump(nums):
    
    memo = dict()

    def bt(index):

        if index >= len(nums) - 1:
            return True

        if index in memo:
            return memo[index]
        
        max_jump = nums[index]
        for jump in range(max_jump, 0, -1):
            if bt(index + jump):
                memo[index] = True
                return True
        
        memo[index] = False
        return False
    
    return bt(0)

print(canJump([2,3,1,1,4]))  # Example usage 
print(canJump([3,2,1,0,4]))  # Example usage       



