"""
REF:
https://leetcode.cn/problems/largest-number-after-digit-swaps-by-parity/solution/by-nehzil-d910/
"""
class Solution:
    def largestInteger(self, num: int) -> int:
        l = [int(d) for d in list(str(num))]   # 转化为各位数值的数组
        n = len(l)
        # sort by condition
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (l[i] - l[j]) % 2 == 0 and l[i] < l[j]:
                    l[i], l[j] = l[j], l[i]

        return int("".join(str(d) for d in l))
