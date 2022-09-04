import sys
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = []

        def dfs(node: TreeNode, row: int, col: int) -> None:
            if not node:
                return None

            nodes.append((row, col, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort(key=lambda s: (s[1], s[0], s[2]))

        matrix, pre_col = [], -sys.maxsize - 1

        for _, col, row_val in nodes:
            if col != pre_col:
                pre_col = col
                matrix.append([])
            matrix[-1].append(row_val)

        return matrix
