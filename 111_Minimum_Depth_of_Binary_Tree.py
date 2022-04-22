# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)
        
        if not root.left or not root.right:
            return left_min + right_min + 1
        else:
            return min(left_min, right_min) + 1
