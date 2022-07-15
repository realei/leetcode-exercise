from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s_color = image[sr][sc]
        if s_color == color:
            return image

        queue = deque([(sr, sc)])
        neighbors = {(1, 0), (0, 1), (-1, 0), (0, -1)}

        while queue:
            row, col = queue.popleft()
            if image[row][col] == s_color:
                image[row][col] = color
            else:
                continue

            for nbr in neighbors:
                n_row = row + nbr[0]
                n_col = col + nbr[1]

                if 0 <= n_row < len(image) and 0 <= n_col < len(image[0]) \
                and image[n_row][n_col] == s_color:
                    queue.append((n_row, n_col))

        return image
