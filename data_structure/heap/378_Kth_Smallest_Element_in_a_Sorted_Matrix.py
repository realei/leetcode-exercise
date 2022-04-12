class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sums = []
        for nums in matrix:
            sums += nums
        heapq.heapify(sums)

        for i in range(k-1):
            heapq.heappop(sums)

        return sums[0]
