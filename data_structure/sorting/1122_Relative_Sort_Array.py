from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt1 = Counter(arr1)
        res = []

        for arr in arr2:
            val = cnt1.pop(arr, None)
            if val:
                res.extend([arr]*val)

        outers = []
        for k, v in cnt1.items():
            outers.extend([k]*v)
            
        if outers:
            outers.sort()
            res.extend(outers)

        return res
