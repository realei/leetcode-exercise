# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def dfs(node: TreeNode, pre_max: int) -> int:

            nonlocal cnt

            if not node:
                return 0
            elif node.val >= pre_max:
                pre_max = node.val
                cnt += 1

            dfs(node.left, pre_max)
            dfs(node.right, pre_max)

            return cnt

        return dfs(root, root.val)
