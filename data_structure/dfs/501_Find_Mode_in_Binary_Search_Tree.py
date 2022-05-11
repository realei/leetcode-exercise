# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        tree_list = []
        
        def dfs(root: TreeNode):
            nonlocal tree_list
            if not root:
                return None
            else:
                tree_list.append(root.val)
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        res_cnt = Counter(tree_list).most_common()

        v, prev_c = res_cnt.pop(0)
        res = [v]
        while res_cnt:
            v, c = res_cnt.pop(0)
            if prev_c == c:
                res.append(v)
            else:
                break
        
        return res
