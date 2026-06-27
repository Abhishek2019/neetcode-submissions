from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row_len = len(grid)
        col_len = len(grid[0])


        fresh = 0
        rotten = 0

        q = deque([])

        for r in range(row_len):
            for c in range(col_len):

                if grid[r][c] == 1:
                    fresh+=1

                if grid[r][c] == 2:
                    rotten+=1
                    q.append((r,c,0))
                    grid[r][c] = -1

        if fresh == 0:
            return 0

        if rotten == 0:
            return -1

        max_yet = -1

        while q:

            r,c,d = q.popleft()

            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:

                nr,nc = r+dr, c+dc

                if 0<=nr<row_len and 0<=nc<col_len and (grid[nr][nc] != -1 and grid[nr][nc] == 1):

                    q.append((nr,nc,d+1))

                    if d+1 > max_yet:
                        max_yet = d+1

                    grid[nr][nc] = -1
                    fresh-=1

        if fresh!=0:
            return -1
        
        return max_yet





        
        





        