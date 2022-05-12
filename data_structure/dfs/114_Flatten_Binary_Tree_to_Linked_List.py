"""
#114. Flatten Binary Tree to Linked List
Time: O(n)
Space: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder_list = []

        def preorderTraversal(root: TreeNode):
            nonlocal preorder_list

            if root:
                preorder_list.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)

        for i in range(1, len(preorder_list)):
            prev, cur = preorder_list[i-1], preorder_list[i]
            prev.left = None
            prev.right = cur
