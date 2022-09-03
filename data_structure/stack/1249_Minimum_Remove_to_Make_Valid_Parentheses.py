class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for k, v in enumerate(s):
            if stack and stack[-1][1] == '(' and v == ')':
                stack.pop()
            elif v in ['(', ')']:
                stack.append((k, v))

        while stack:
            k, _ = stack.pop()
            s = s[0:k] + s[k+1:]

        return s
