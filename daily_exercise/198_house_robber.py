"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        fk_2 = 0
        fk_1 = nums[0]

        for i in range(1, len(nums)):
            fk = max(fk_1, fk_2 + nums[i])
            fk_2, fk_1 = fk_1, fk

        return fk
