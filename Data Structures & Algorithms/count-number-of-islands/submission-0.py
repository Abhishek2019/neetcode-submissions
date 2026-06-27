from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.count = 0
        self.rows  = len(grid)
        self.cols  = len(grid[0])

        self.visited = [[0]*self.cols for _  in range(self.rows)]

        

        for r in range(self.rows):
            for c in range(self.cols):

                if grid[r][c] == "1" and self.visited[r][c] == 0:

                    q = deque([(r,c)])
                    self.visited[r][c] = 1

                    while q:

                        x,y = q.popleft()

                        for dx, dy in [(0,-1), (-1,0),(0,1),(1,0)]:

                            nx, ny = x+dx,y+dy

                            if 0<= nx<= self.rows-1 and 0<= ny<= self.cols-1 and self.visited[nx][ny] == 0 and grid[nx][ny] == "1":

                                q.append((nx,ny))
                                self.visited[nx][ny] = 1
                    
                    self.count+=1

        return self.count