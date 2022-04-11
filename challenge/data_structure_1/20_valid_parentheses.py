"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution:
    OPEN_DICT = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    def isValid(self, s: str) -> bool:
        res_stack = []
        if len(s) == 0 or len(s) % 2 != 0:
            return False

        for i in s:
            if i in self.OPEN_DICT.values():
                res_stack.append(i)
            elif i in self.OPEN_DICT.keys():
                if not res_stack:
                    return False
                else:
                    last = res_stack.pop()
                if self.OPEN_DICT.get(i) != last:
                    return False

        return True if not res_stack else False
