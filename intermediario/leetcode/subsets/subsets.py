
def subsets(nums):
    output = []

    def bt(partial, index):

        output.append(partial[:])
        for i in range(index, len(nums)):
            partial.append(nums[i])
            bt(partial, i+1)    
            partial.pop(-1)
            
    
    bt([], 0)
    return output
        