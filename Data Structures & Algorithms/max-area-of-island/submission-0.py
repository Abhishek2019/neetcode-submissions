from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.max_area = 0
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.visited = [[0]*self.cols for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):

                if self.visited[r][c] == 0 and grid[r][c] == 1:

                    q = deque([(r,c)])
                    self.visited[r][c] = 1

                    local_count = 1

                    while q:

                        x,y = q.popleft()

                        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:

                            nx, ny = x+dx, y+dy


                            if 0<=nx<self.rows and 0<=ny<self.cols and self.visited[nx][ny] == 0 and grid[nx][ny]  == 1:
                                q.append((nx,ny))
                                self.visited[nx][ny] = 1
                                local_count+=1

                    if local_count>self.max_area:
                        self.max_area = local_count

        return self.max_area


                        


