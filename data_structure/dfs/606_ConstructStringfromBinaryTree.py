from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return None

            nonlocal res
            res += str(node.val)

            if not node.left and node.right:
                res += "()"

            if node.left:
                res += "("
                dfs(node.left)
                res += ')'
            if node.right:
                res += '('
                dfs(node.right)
                res += ')'

        dfs(root)
        return res
