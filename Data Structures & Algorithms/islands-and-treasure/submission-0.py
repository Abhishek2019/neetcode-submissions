
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        row_len = len(grid)
        col_len = len(grid[0])

        

        for r in range(row_len):
            for c in range(col_len):


                if grid[r][c] == 0:

                    q = deque([((r,c,0))])
                    visited = [[0]*col_len for _ in range(row_len)]

                    visited[r][c] = 1

                    while q:

                        r1,c1,d1 = q.popleft()

                        for dr,dc in [(-1,0), (1,0), (0,1), (0,-1)]:

                            nr,nc = r1+dr, c1+dc

                            if 0<=nr<=row_len-1 and 0<=nc<=col_len-1 and visited[nr][nc] == 0:


                                if grid[nr][nc] == -1:
                                    pass

                                elif grid[nr][nc] == 2147483647:

                                    grid[nr][nc] = d1+1
                                    q.append((nr,nc,d1+1))
                                    visited[nr][nc] = 1


                                elif grid[nr][nc] == 0:
                                    pass

                                else:
                                    if grid[nr][nc] > d1+1:
                                        grid[nr][nc] = d1+1
                                        q.append((nr,nc,d1+1))
                                        visited[nr][nc] = 1


                                    

                                

                                



                            











