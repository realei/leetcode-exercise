from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = [(-v, k) for k, v in Counter(nums).items()]
        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
            
        return res
