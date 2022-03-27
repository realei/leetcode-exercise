class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for i in range(1, len(s)):
            if not stack:
                stack.append(s[i])
            elif stack[-1] != s[i] and stack[-1].upper() == s[i].upper():
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)

