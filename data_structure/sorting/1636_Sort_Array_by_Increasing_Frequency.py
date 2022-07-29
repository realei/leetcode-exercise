"""
Note(Must Read):
[Python 3 solution - with process of thinking and improvement](https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/1065249/Python-3-solution-with-process-of-thinking-and-improvement)
"""

from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        r = Counter(nums)
        return sorted(nums, key=lambda x: (r[x], -x))
