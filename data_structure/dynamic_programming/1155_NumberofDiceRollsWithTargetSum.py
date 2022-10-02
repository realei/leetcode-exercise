"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355894/Python-DP-with-memoization-explained

https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/solution/yi-pian-wen-zhang-chi-tou-bei-bao-wen-ti-rsy8/
"""


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]
            to_return = 0
            for k in range(max(0, target-f), target):
                to_return += dp(d-1, k)
            memo[(d, target)] = to_return
            return to_return
        return dp(d, target) % (10**9 + 7)
