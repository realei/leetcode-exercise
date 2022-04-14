class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [0]*len(score)
        medal_dict = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
            }

        maxHeap = [(-v, k) for k, v in enumerate(score)]
        heapq.heapify(maxHeap)

        ranking = 0
        while maxHeap:
            _, idx = heapq.heappop(maxHeap)
            res[idx] = medal_dict.get(ranking) if ranking <= 2 else str(ranking+1)

            ranking += 1

        return res
