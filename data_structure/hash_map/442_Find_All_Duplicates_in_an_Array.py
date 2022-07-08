from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        nums_cnt = Counter(nums)
        res = []
        for key in nums_cnt:
            if nums_cnt[key] == 2:
                res.append(key)
        
        return res
