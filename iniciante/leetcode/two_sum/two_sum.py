
# Usar mapa de hash para pegar complexidade melhor (Dicas do lletcodee)

class Solution(object):
    def twoSum(self, nums, target):
        
        mapa = {}

        for index, num in enumerate(nums):
            
            complemento = target - num

            if mapa.get(complemento) != None:
                return [mapa[complemento], index]

            mapa[num] = index


#teste

solution = Solution()

print(solution.twoSum([3,3],6))