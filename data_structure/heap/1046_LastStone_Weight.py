class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        for i in range(len(stones)):
            stones[i] = - stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            m = -heapq.heappop(stones)
            n = -heapq.heappop(stones)

            if m != n:
                heapq.heappush(stones, -(m-n))
            else:
                pass
        
        return -stones[0] if stones else 0
