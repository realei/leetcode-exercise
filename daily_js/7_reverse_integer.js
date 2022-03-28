/**
 * https://leetcode.com/problems/reverse-integer/
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {

    let splitString = x.toString().split("").reverse();
    let res = 0
    
    if (splitString[splitString.length -1] === '-') {
        splitString.pop();
        splitString = splitString.join("");
        res = -parseInt(splitString);
    } else {
        splitString = splitString.join("");
        res = parseInt(splitString);
    };

    if (res < 0 - 2**31 || res > 2**31 -1) {
        res = 0
    };
    
    return res;
    
};
