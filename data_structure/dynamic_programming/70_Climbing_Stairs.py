class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1;
        
        p, q, s = 1, 1, 1
        
        for i in range(2, n + 1):
            p, q = q, s
            s = p + q
        
        return s
