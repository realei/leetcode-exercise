class Solution:
    def findErrorNums(self, nums):
        ln, total = len(nums), sum(set(nums))
        return [sum(nums) - total, (1 + ln) * ln // 2 - total]

"""
hash map
"""
# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         nums_cnt = collections.Counter(nums)
#         res = [0, 0]
#         for i in range(1, len(nums)+1):
#             if nums_cnt[i] == 2:
#                 res[0] = i
#             elif nums_cnt[i] == 0:
#                 res[1] = i
#         return res
