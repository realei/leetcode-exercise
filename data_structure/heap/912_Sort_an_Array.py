class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        res = []
        heapq.heapify(nums)
        while nums:
            res.append(heapq.heappop(nums))
        
        return res
