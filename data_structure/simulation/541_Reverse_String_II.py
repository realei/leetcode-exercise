class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(t), 2*k):
            t[i:i+k] = reversed(t[i:i+k])
        
        return "".join(t)
        
"""
Note: (we have to change str to list)
>>> s[0:2] = reversed(s[0:2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
"""
