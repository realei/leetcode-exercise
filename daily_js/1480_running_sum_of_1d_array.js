/**
 * https://leetcode.com/problems/running-sum-of-1d-array/
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    
    nums.forEach( (element, index, array) => {
        if (index !== 0) { 
            array[index] += array[index - 1];
        }
    });
    
    return nums;
    
};
