from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pruneNode(node: Optional[TreeNode]) -> bool:
            if not node:
                return False

            left = pruneNode(node.left)
            right = pruneNode(node.right)

            if not left:
                node.left = None
            if not right:
                node.right = None

            return node.val == 1 or left or right

        return root if pruneNode(root) else None
