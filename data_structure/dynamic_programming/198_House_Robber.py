from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return max(nums)

        left, right = nums[0], max(nums[0], nums[1])

        for i in range(2, length):
            left, right = right, max(right, left + nums[i])

        return right
