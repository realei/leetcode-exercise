from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue, res = [root], []

        while queue:
            res.append([node.val for node in queue])
            cnt = len(queue)

            while cnt != 0:
                cnt -= 1
                node = queue.pop(0)
                queue += [child for child in node.children if child]

        return res
