# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        
        def maxDepth(root:[TreeNode]) -> int:
            nonlocal longest
            
            if not root:
                return 0
            
            left_max = maxDepth(root.left)
            right_max = maxDepth(root.right)
            
            longest = max(left_max + right_max, longest)
            
            return max(left_max, right_max) + 1
        
        maxDepth(root)
        return longest
