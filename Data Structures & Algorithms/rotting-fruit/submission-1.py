from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        minutes_mat = [[0]*col_len for _ in range(row_len)]
        fresh = 0

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1:
                    fresh += 1

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 2:
                    q = deque([(r, c, 0)])
                    visited = [[0]*col_len for _ in range(row_len)]
                    visited[r][c] = 1

                    while q:
                        r1, c1, d1 = q.popleft()

                        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                            nr, nc = r1 + dr, c1 + dc

                            if 0 <= nr < row_len and 0 <= nc < col_len and visited[nr][nc] == 0:
                                visited[nr][nc] = 1

                                if grid[nr][nc] == 1:
                                    if minutes_mat[nr][nc] == 0 or (d1 + 1 < minutes_mat[nr][nc]):
                                        minutes_mat[nr][nc] = d1 + 1
                                        q.append((nr, nc, d1 + 1))

        # If there were no fresh oranges, answer is 0
        if fresh == 0:
            return 0

        # If any fresh orange never got a minute assigned, it's unreachable => -1
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1 and minutes_mat[r][c] == 0:
                    return -1

        return max(map(max, minutes_mat))
