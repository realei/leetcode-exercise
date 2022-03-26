class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        cur_size, max_size = 0, 0
        for c in s:
            if c == "(":
                stack.append(c)
                cur_size+=1
            elif c == ")":
                stack.pop()
                cur_size-=1
            else:
                continue
                
            max_size = max(cur_size, max_size)
        return max_size
