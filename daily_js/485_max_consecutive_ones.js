/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let [cur, max] = [0, 0];
    nums.forEach((value) => {
        if (value === 1) {
            cur += 1;
        } else {
            cur = 0;
        }
        max = Math.max(cur, max);
    })
    return max;
};
