class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for k, v in enumerate(s):
            if stack and stack[-1][1] == "(" and v == ")":
                stack.pop()
            elif v == "(" or v == ")":
                stack.append((k,v))
        
        while stack:
            index, _ = stack.pop()
            if len(s) > index:
                s = s[0 : index : ] + s[index + 1 : :]
        
        return s  
