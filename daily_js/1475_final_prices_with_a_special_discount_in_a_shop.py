"""
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
"""
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        queue = []
        result = [0]*len(prices)
        for k, v in enumerate(prices):
            if queue and v <= queue[-1][1]:
                while queue and v <= queue[-1][1]:
                    key, val = queue.pop()
                    result[key] = val - v
                    
            queue.append((k, v))
        
        while queue:
            key, val = queue.pop(0)
            result[key] = val
        
        return result
