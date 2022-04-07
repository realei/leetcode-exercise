/**
 * @param {number} n
 * @return {boolean}
 */
var isUgly = function(n) {
    if (n <= 0) {
        return false;
    }
    let primeFactors = [2,3, 5];
    
    for (let factor of primeFactors) {
        while (n % factor === 0) {
            n /= factor;
        }
    }
    
    return n === 1;
};
