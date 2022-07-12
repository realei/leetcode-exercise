"""
Reference:
https://leetcode.cn/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/
"""
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(grid: List[List[int]], i: int, j: int) -> int:
            queue = [[i, j]]
            count = 0
            while queue:
                [i, j] = queue.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) \
                        and grid[i][j] == 1:
                    grid[i][j] = 0
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
                    count += 1
            return count

        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            if row[0]:
                bfs(grid, i, 0)
            if row[n - 1]:
                bfs(grid, i, n-1)
        for j in range(1, n-1):
            if grid[0][j]:
                bfs(grid, 0, j)
            if grid[m - 1][j]:
                bfs(grid, m - 1, j)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                res += bfs(grid, i, j)
        return res
