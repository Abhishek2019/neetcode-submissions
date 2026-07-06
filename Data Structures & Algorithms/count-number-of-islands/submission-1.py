from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        visited = set()
        rlen = len(grid)-1
        clen = len(grid[0])-1
        
        
        count = 0
        for ridx in range(len(grid)):
            for cidx in range(len(grid[0])):

                if (ridx,cidx) not in visited:
                    visited.add((ridx,cidx))

                    if grid[ridx][cidx] == "1":
                        q = deque([(ridx,cidx)])
                        count+=1
                        while q:

                            curr_x,curr_y = q.pop()

                            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:

                                nx,ny = curr_x+dx, curr_y+dy

                                if 0<=nx<=rlen and 0<=ny<=clen:
                                
                                    if (nx,ny) not in visited and grid[nx][ny] == "1":
                                        visited.add((nx,ny))
                                        q.append((nx,ny))
                                    else:
                                        visited.add((nx,ny))

        return count














