from typing import List
"""
# Note: can's use Two Pointers
```
Corner Case can't passed by two pointers:
"abcd"
["a","abc","b","cd"]
```
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #corner case: len(s) <= 2
        if len(s) <= 2:
            if s in wordDict:
                return True 
            elif s[0] in wordDict and s[1] in wordDict:
                return True
            
        l, r = 0, 2
        while r < len(s):
            if s[l:r] in wordDict:
                l = r
            r = r + 1
        # now `r` should be l`length +1`
        return s[l:r] in wordDict
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]
