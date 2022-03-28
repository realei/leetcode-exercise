/**
 * https://leetcode.com/problems/add-digits/
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    let res = 0;
    while (num!==0 || res > 9) {
        if (num !== 0 ) {
            res += num % 10;
            num = Math.floor(num/10)
        } else if (res > 9) {
            num = res;
            res = 0;
        }

    };
    return res;
}
