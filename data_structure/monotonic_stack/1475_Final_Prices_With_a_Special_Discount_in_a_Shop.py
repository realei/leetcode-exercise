from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = []
        stack = [0]

        for i in range(n - 1, -1, -1):
            while len(stack) > 1 and stack[-1] > prices[i]:
                stack.pop()
            res.insert(0, prices[i] - stack[-1])
            stack.append(prices[i])

        return res
