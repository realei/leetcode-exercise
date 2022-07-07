class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        BFS Solution
        """
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                q = collections.deque([(i, j)])
                if grid[i][j] == '0': 
                    continue
                while q:
                    cur_i, cur_j = q.popleft()
                    if grid[cur_i][cur_j] != '1':
                        continue
                    grid[cur_i][cur_j] = '0'
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        
                        if next_i < 0 or next_j < 0 or next_i == len(grid) or next_j == len(grid[0]):
                            continue
                        if grid[next_i][next_j] == '1':
                            q.append((next_i, next_j))
                ans += 1
        return ans
                
# class Solution:
#     def numIslands(self, grid: [[str]]) -> int:
#         def bfs(grid, i, j):
#             queue = [[i, j]]
#             while queue:
#                 [i, j] = queue.pop(0)
#                 if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
#                     grid[i][j] = '0'
#                     queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '0': continue
#                 bfs(grid, i, j)
#                 count += 1
#         return count

