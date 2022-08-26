from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dst, n = 0, len(nums)

        for i in range(n):
            max_dst = max(i + nums[i], max_dst)
            if max_dst >= n - 1:
                return True

        return False
