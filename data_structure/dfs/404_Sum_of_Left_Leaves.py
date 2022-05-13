# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        isLeafNode = lambda node: not node.left and not node.right
        
        def dfs(node: TreeNode):
            res = 0
            
            if node.left:
                res += node.left.val if isLeafNode(node.left) else dfs(node.left)
            if node.right and not isLeafNode(node.right):
                res += dfs(node.right)
            return res
        
        return dfs(root) if root else 0
