from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = set()

        def dfs(val: int, layers: int) -> None:
            if val == 0:
                return None

            left, right = val % 10 - k, val % 10 + k
            layers -= 1

            if layers == 1:
                res.update({val*10 + left}) if left >= 0 else None
                res.update({val*10 + right}) if right < 10 else None
                return None

            dfs(val*10 + left, layers) if left >= 0 else None
            dfs(val*10 + right, layers) if right < 10 else None

            return None

        roots = [i for i in range(9, k - 1, -1)] + \
            [9 - i for i in range(k, 9, 1)]

        for root in roots:
            dfs(root, n)

        return list(res)
