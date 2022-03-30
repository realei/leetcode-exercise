"""
https://leetcode.com/problems/find-common-characters/
"""

from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = None
        for a in words:
            c = Counter(a)
            if res is None:
                res = c
            else:
                res &= c
        return list(res.elements())
