class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []

        for dir in dirs:
            if dir == "..":
                stack.pop() if stack else None
            elif dir != '.' and dir:
                stack.append(dir)

        return '/' + '/'.join(stack)
