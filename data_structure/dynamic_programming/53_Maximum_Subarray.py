from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, pre_sum = nums[0], nums[0]
        for i in range(1, len(nums)):

            pre_sum = pre_sum + nums[i] if pre_sum + \
                nums[i] > nums[i] else nums[i]
            max_sum = max_sum if max_sum > pre_sum else pre_sum

        return max_sum
