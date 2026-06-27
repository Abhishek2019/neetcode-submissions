from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row_len = len(heights)
        col_len = len(heights[0])


        pacific = [(0,i) for i in range(col_len)] + [(i,0) for i in range(row_len)]
        atlantic =  [(row_len-1,i) for i in range(col_len)] + [(i,col_len-1) for i in range(row_len)]

        pacific = set(pacific)
        atlantic = set(atlantic)

        # pacific check

        visited_by_pacific = pacific

        q = deque(pacific)

        while q:

            r,c = q.popleft()

            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:

                nr, nc = r+dr, c+dc

                if 0<=nr< row_len and 0<=nc<col_len and (nr,nc) not in visited_by_pacific:
                    if heights[r][c] <= heights[nr][nc]:

                        visited_by_pacific.add((nr,nc))
                        q.append((nr,nc))

        # atlantic check

        visited_by_atlantic = atlantic

        q = deque(atlantic)

        while q:

            r,c = q.popleft()

            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:

                nr, nc = r+dr, c+dc

                if 0<=nr< row_len and 0<=nc<col_len and (nr,nc) not in visited_by_atlantic:
                    if heights[r][c] <= heights[nr][nc]:

                        visited_by_atlantic.add((nr,nc))
                        q.append((nr,nc))


        final = [[r,c] for r,c in visited_by_pacific & visited_by_atlantic]
        return final


