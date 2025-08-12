



def rob(nums):

   if len(nums) == 1:
      return nums[0]
   if len(nums) == 2:
      return max(nums)
    
   def rob_one(nums):
      memo = dict()

      print(memo)
      print(nums)

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


   return max(rob_one(nums[:-1]), rob_one(nums[1:]))    


print(rob([1,2]))  # Example usage