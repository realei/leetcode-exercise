/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let n = nums.length;
    let ans = [];
    
    let i = 0;
    let j = n -1;
    
    while (i <= j) {
        if (nums[i]**2 > nums[j]**2) {
            ans.unshift(nums[i]**2);
            i++;
        } else {
            ans.unshift(nums[j]**2);
            j--;
        };
    };
    return ans;
    
};
