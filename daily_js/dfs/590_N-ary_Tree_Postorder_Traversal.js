/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[]}
 */
let postorder = function(root) {
    let res = [];
    helper(root, res);
    return res;
};

let helper = (root, res) => {
    if (root === null) {
        return null;
    }
    for (let ch of root.children) {
        helper(ch, res);
    }
    res.push(root.val);
}
