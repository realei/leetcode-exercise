from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.num = 0
        self.inOrderDFS(root)

        return self.num

    def inOrderDFS(self, root):
        if not root:
            return
        # First traversal to leftist leave, find the minimum value
        self.inOrderDFS(root.left)

        self.k -= 1
        if self.k == 0:
            self.num = root.val
            return

        self.inOrderDFS(root.right)
