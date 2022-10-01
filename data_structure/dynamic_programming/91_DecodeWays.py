class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp_2, dp_1 = 0, 1
        for i in range(1, n + 1):
            dp = 0
            if s[i-1] != '0':
                dp += dp_1
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                dp += dp_2
            dp_2, dp_1 = dp_1, dp
        return dp
