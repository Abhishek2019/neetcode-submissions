from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        row_len = len(board)
        col_len = len(board[0])

        corner_zero = set()

        for r in range(row_len):
            for c in range(col_len):

                if r == 0 or r == row_len-1 or c == 0  or c == col_len-1:
                    
                    if board[r][c] == 'O':

                        corner_zero.add((r,c))

        q = deque(corner_zero)
        vis = corner_zero

        while q:

            r,c = q.popleft()

            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:

                nr, nc = r+dr, c+dc
                
                if (0<=nr<row_len-1) and  (0<=nc<col_len-1) and ((nr,nc) not in vis):

                    if board[nr][nc] == 'O':
                        
                        q.append((nr,nc))
                        vis.add((nr,nc))


        for r in range(row_len):
            for c in range(col_len):

                if (r,c) not in vis and board[r][c] == 'O':
                    board[r][c] = 'X'





