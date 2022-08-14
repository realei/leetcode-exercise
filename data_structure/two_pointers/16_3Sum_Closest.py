from typing import List
import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        diff_min, sum_min = sys.maxsize, sum(nums[:3])

        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr > target:
                    right -= 1
                elif curr == target:
                    return curr
                else:
                    left += 1

                if diff_min > abs(curr - target):
                    diff_min = abs(curr - target)
                    sum_min = curr

        return sum_min
