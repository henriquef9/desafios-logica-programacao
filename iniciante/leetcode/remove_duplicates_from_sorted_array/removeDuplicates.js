
var removeDuplicates = function(nums) {
    
    let left = 0

    for (let right = 0; right < nums.length; right++) {
        const element = nums[right];

        if (element != nums[left]){
            left++
            nums[left] = nums[right]
        }
        
    }

    return left+1
};


console.log(removeDuplicates([1,1,2]))