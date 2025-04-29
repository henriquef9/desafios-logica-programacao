/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    l = 0;
    r = nums.length - 1;

    while(l < r){


        if(nums[l] != 2 && nums[l] != 1){
            l+=1;
        }

        if(nums[r] != 0){
            r-=1;
        }
        
        if((nums[l] == 2 || nums[l] == 1) && nums[r] == 0 && l < r){
            let aux = nums[l];
            nums[l] = nums[r];
            nums[r] = aux;
            l+=1;
            r-=1;
        }
    }

    l = 0;
    r = nums.length - 1;

    while(l < r){

        if(nums[l] != 2){
            l+=1;
        }

        if(nums[r] != 1){
            r-=1;
        }

        if(nums[l] == 2 && nums[r] == 1 && l < r){
            let aux = nums[l];
            nums[l] = nums[r];
            nums[r] = aux;            
            l+=1;
            r-=1;       
        }
    }

    return nums
};

// teste
        
var nums = [0,1];

console.log(sortColors(nums));