import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        heap = [1]
        ugly_set = set([1])

        for i in range(n):
            val = heapq.heappop(heap)

            for j in factors:
                ugly_num = val*j
                if ugly_num not in ugly_set:
                    heapq.heappush(heap, ugly_num)
                    ugly_set.add(ugly_num)

        return val
