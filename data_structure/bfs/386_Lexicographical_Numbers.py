from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(num: int, target: int) -> List[int]:
            if num > target:
                return
            res.append(num)
            for i in range(10):
                dfs(num*10 + i, target)

        # start from the second layer of the Tree
        for num in range(1, 10):
            dfs(num, n)

        return res
