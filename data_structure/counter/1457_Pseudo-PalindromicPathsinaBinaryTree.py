from collections import Counter
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def isCntPalindromic(cnt: Counter) -> bool:
            """
            1 <= Node.val <= 9
            """
            odd = 0
            for _, v in cnt.items():
                if v % 2 == 1:
                    odd += 1
                    if odd > 1:
                        return False
            return True

        count, cnt = 0, Counter()

        def dfs(node, cnt: Counter) -> None:
            nonlocal count
            if not node:
                return None
            cnt[node.val] += 1
            if not node.left and not node.right:
                if isCntPalindromic(cnt):
                    count += 1
                cnt[node.val] -= 1
                return None
            dfs(node.left, cnt)
            dfs(node.right, cnt)
            cnt[node.val] -= 1

        dfs(root, cnt)

        return count
