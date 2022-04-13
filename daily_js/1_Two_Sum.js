/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    numsDict = new Map();

    nums.forEach((value, index) => {
        numsDict.set(value, index);
    })

    for (let i=0; i<nums.length; i++) {
        if(numsDict.get(target - nums[i]) && i !== numsDict.get(target - nums[i])) {
            return [i, numsDict.get(target - nums[i])];
        }
    }

    return []

};
