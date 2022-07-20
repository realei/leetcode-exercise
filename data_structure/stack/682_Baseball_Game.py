from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = [int(ops[0])]
        for i in range(1, len(ops)):
            if ops[i] == 'C':
                stack.pop()
            elif ops[i] == 'D':
                stack.append(2*stack[-1])
            elif ops[i] == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(ops[i]))

        return sum(stack)
