class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Solution: stack
        """

        def calStr(s: str) -> str:
            stack = []
            for i in range(len(s)):
                if s[i] != "#":
                    stack.append(s[i])
                elif stack:
                    stack.pop()
            return "".join(stack)

        return calStr(s) == calStr(t)
