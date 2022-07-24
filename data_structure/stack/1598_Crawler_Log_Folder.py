from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        for i in range(len(logs)):
            if logs[i] == "./":
                continue
            elif logs[i] == "../" and steps == 0:
                continue
            elif logs[i] == "../":
                steps -= 1
            else:
                steps += 1
        return steps
