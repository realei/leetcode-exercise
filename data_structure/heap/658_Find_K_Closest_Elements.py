class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        min_heap = [(abs(x - num), num) for num in arr]
        heapq.heapify(min_heap)
        res = []

        while k:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1

        res.sort()
        return res
