from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        s_cnt = Counter(s)
        max_heap = [(-v, k) for k, v in s_cnt.items()]
        res = []
        heapq.heapify(max_heap)
        while max_heap:
            num, chr = heapq.heappop(max_heap)
            res.append(chr*-num)
        
        return ("").join(res)
