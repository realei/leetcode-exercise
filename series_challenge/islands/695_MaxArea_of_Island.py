"""
https://leetcode.com/problems/max-area-of-island/
Solution: DFS
Reference: https://leetcode.cn/problems/number-of-islands/solution/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def inArea(grid: List[List[int]], row: int, col: int) -> bool:
            return 0 <= row and row < len(grid) and 0 <= col and col < len(grid[0])

        def dfsArea(grid: [List[int]], row: int, col: int) -> None:
            if not inArea(grid, row, col):
                return 0

            if grid[row][col] != 1:
                return 0

            grid[row][col] = 2

            return 1 + dfsArea(grid, row - 1, col) \
                + dfsArea(grid, row + 1, col) \
                + dfsArea(grid, row, col - 1) \
                + dfsArea(grid, row, col + 1)

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res = max(res, dfsArea(grid, row, col))

        return res
