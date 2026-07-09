from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        rlen = len(grid)
        clen = len(grid[0])
        
        q = deque([])
        for r in range(rlen):
            for c in range(clen):

                if grid[r][c] == 0:
                    q.append((r,c))

                
        while q:

            curr_x, curr_y = q.pop()

            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:

                nx,ny = curr_x+dx, curr_y+dy

                if 0<=nx<rlen and 0<=ny<clen:

                    if grid[nx][ny] == -1:
                        continue
                    
                    if grid[nx][ny] !=0:
                        
                        if (grid[curr_x][curr_y] + 1) < grid[nx][ny]: 
                            grid[nx][ny] = grid[curr_x][curr_y] + 1
                            q.append((nx,ny))

        


