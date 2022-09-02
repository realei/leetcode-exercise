from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        cur_cnt = 1
        level_avg = []

        while queue:
            cnt, sum = 0, 0
            for i in range(cur_cnt):
                node = queue.pop(0)
                sum += node.val

                if node.left:
                    queue.append(node.left)
                    cnt += 1

                if node.right:
                    queue.append(node.right)
                    cnt += 1

            level_avg.append(sum/cur_cnt)
            cur_cnt = cnt

        return level_avg
