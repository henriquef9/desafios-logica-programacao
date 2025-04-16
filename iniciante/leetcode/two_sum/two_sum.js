
// Usar mapa de hash para pegar complexidade melhor (Dicas do lletcodee)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    let result = []

    nums.forEach((num, index, nums) => {
        
        for(i = index + 1; i < nums.length; i++){

            if(target === (num + nums[i])){
                result = [index, i]
            }
        }

    })

    return result 

};

// Teste

nums = [3,3]
target = 6

console.log(twoSum(nums, target))