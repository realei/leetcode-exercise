"""
https://leetcode.com/problems/divide-array-into-equal-pairs/
"""

from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_cnt = Counter(nums)
        for _, v in nums_cnt.items():
            if v%2 != 0:
                return False
        return True
