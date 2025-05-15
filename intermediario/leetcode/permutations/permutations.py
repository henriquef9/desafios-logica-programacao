def permute(nums):
    
    output = []

    def bt(partial):

        if len(nums) == len(partial):
            output.append(partial[:])
        else:
            for element in nums:
                if element in partial:
                    continue
                partial.append(element)
                bt(partial)
                partial.pop(-1)
        
    
    bt([])
    return output


print(*permute([1,2,3]))