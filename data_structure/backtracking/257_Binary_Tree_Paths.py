"""
Backtracking: 
[【递归回溯】朴素的思路，套路的步骤，+Debug代码](https://leetcode.cn/problems/binary-tree-paths/solution/di-gui-hui-su-po-su-de-si-lu-tao-lu-de-bu-zou-debu/)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def backtrace(root, path):
            if not root:
                return []
            path.append(root.val)
            if not root.right and not root.left:
                res.append(path[:])
                return
            choices = []
            if root.left:
                choices.append(root.left)
            if root.right:
                choices.append(root.right)
            for choice in choices:
                 backtrace(choice, path)
                 path.pop()
        res = []
        backtrace(root, [])
        return ["->".join(list(map(str,i))) for i in res]
