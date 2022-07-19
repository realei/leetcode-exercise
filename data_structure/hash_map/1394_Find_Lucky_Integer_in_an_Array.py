from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr:List[int]) -> int:
        arr_cnt = Counter(arr)
        ans = -1
        for k, v in arr_cnt.items():
            if k == v:
                ans = max(ans, k)
        return ans
