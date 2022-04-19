class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        min_heap = [(sum(row), idx) for idx, row in enumerate(mat)]
        heapq.heapify(min_heap)
        res = []

        while k:
            k -= 1
            res.append(heapq.heappop(min_heap)[1])
        
        return res
