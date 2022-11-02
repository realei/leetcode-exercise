class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def touchArea(grid: List[List[int]], row: int, col: int) -> bool:
            # return 0 > row or row >= len(grid) or 0 > col or col >= len(grid[0])
            return row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])

        def dfs(grid: List[List[int]], row: int, col: int) -> bool:
            if touchArea(grid, row, col):
                return 0

            if grid[row][col] == 1:
                return 1

            grid[row][col] = 1

            return dfs(grid, row+1, col)\
                * dfs(grid, row-1, col)\
                * dfs(grid, row, col+1)\
                * dfs(grid, row, col-1)

        # cnt = 0
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == 0 and dfs(grid, row, col):
        #             cnt += 1
        # return cnt
        return sum(dfs(grid, i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if not cell)
