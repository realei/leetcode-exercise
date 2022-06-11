/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
// var intersection = function(nums1, nums2) {
    
//     let nums1Set = new Set(nums1);
//     let nums2Set = new Set(nums2);
//     if (nums1Set.size > nums2Set.size) {
//         [nums1Set, nums2Set] = [nums2Set, nums1Set];
//     }
    
//     let result = new Set();
    
//     nums1Set.forEach((element, index, set) => {
//         if (nums2Set.has(element)) {
//             result.add(element);
//         };
//     });
    
//     return [...result];
    
// };

var intersection = function(nums1, nums2) {
    let nums1Set = new Set(nums1);
    let nums2Set = new Set(nums2);
    let result = new Set([...nums1Set].filter(x => nums2Set.has(x)));
    
    return result = [...result]
}
