"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.
"""

from collections import Counter
class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        res = sorted(Counter(nums).keys(), reverse=True)

        return res[ 2 if len(res) > 2 else 0]
