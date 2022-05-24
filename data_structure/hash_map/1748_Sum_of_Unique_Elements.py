from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_cnt = Counter(nums)

        res = 0
        for v, n in nums_cnt.items():
            if n == 1:
                res += v
        
        return res

# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#         return sum(num  for num,time in collections.Counter(nums).items() if time == 1)
