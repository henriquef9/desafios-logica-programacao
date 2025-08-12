

def rob(nums):
    
   memo = dict()

   def bt(index):
      
      if index in memo:
         return memo[index]

      if index == 0:
         memo[index] = nums[index]
      elif index == 1:
         memo[index] = max(nums[index-1], nums[index])
      else:
         memo[index] = max(nums[index] + bt(index - 2), bt(index - 1))

      return memo[index]

   max_value = 0

   for i in range(len(nums) -1 , -1, -1):
      max_value = max(max_value, bt(i))

   return max_value    


print(rob([2,7,9,3,1]))  # Example usage