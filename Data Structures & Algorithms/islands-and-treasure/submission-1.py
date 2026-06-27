from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        inf = 2147483647

        row = len(grid)
        col = len(grid[0])

        q = deque([])

        for r in range(row):
            for c in range(col):

                if grid[r][c] == 0:

                    q.append((r,c,0))

        while q:

            r,c,dist = q.popleft()

            for dr,dc in [(-1,0),(1,0), (0,1), (0,-1)]:

                nr,nc = r+dr, c+dc

                ndist = dist+1

                if 0<=nr<row and 0<=nc<col and grid[nr][nc] != -1 and grid[nr][nc]!=0 and ndist< grid[nr][nc]:
                    grid[nr][nc] = ndist

                    q.append((nr,nc,ndist))

        





