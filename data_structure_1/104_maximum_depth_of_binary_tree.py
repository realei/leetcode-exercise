"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_depth = 0
        if not root:
            return max_depth

        stack = [root]

        while stack:
            m = len(stack)
            for _ in range(m):
                node = stack.pop(0)

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            max_depth += 1


        return max_depth
