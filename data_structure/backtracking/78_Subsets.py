"""
Ref:
1. leetcode cn: https://leetcode.cn/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/
2. leetcode en: https://leetcode.com/problems/subsets/discuss/780493/python3-backtrack-algorithm
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(cur,pos):
            # if pos>n:
            #     return 
            
            res.append(cur[:])
            if pos==n:
                return
            for i in range(pos,n):
                cur.append(nums[i])
                backtrack(cur,i+1)
                cur.pop()
            
        backtrack([],0)
        return res
