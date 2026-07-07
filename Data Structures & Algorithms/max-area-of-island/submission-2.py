from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rlen = len(grid)
        clen = len(grid[0])

        visited=set()
        max_area = 0
        for r in range(rlen):
            for c in range(clen):

                if (r,c) not in visited:
                    visited.add((r,c))

                    if grid[r][c] == 1:

                        curr_area = 1

                        q = deque([(r,c)])

                        while q:

                            curr_r, curr_c = q.pop()

                            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:

                                nr,nc = curr_r+dr, curr_c+dc

                                if 0<=nr<=rlen-1 and 0<=nc<=clen-1:

                                    if (nr,nc) not in visited:
                                        if grid[nr][nc] == 1:
                                            q.append((nr,nc))
                                            curr_area+=1

                                        visited.add((nr,nc))

                        max_area = max(max_area, curr_area)
        return max_area
                                    

                                    

                                        

                                    





        