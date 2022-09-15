from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt = Counter(changed)
        if cnt[0] % 2:
            return []

        for x in sorted(cnt):
            if cnt[x] > cnt[2*x]:
                return []
            cnt[2*x] -= cnt[x] if x else int(cnt[x] / 2)

        return list(cnt.elements())
