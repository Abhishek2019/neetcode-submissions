from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rlen = len(grid)
        clen = len(grid[0])

        q = deque([])

        visited = set()

        final_count = 0
        max_time = 0

        for r in range(rlen):
            for c in range(clen):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c,0))
                if grid[r][c] == 1:
                    final_count+=1

        while q:

            curr_x, curr_y, curr_lev = q.popleft()
            max_time = max(max_time, curr_lev)

            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:

                nx,ny = curr_x+dx, curr_y+dy

                if 0<=nx<rlen and 0<=ny<clen:

                    if (nx,ny) not in visited:
                        visited.add((nx,ny))
                        if grid[nx][ny] == 1:
                            
                            q.append((nx,ny,curr_lev+1))

                            final_count-=1
        if final_count!=0:
            return -1
        
        return max_time


                        