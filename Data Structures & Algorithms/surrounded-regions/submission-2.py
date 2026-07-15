from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rlen = len(board)
        clen = len(board[0])

        corner_zero = set()
        visited = set()

        for r in range(rlen):
            for c in range(clen):

                if (r,c) not in visited:

                    if board[r][c] == 'O' and (r  in (0,rlen-1) or c  in (0,clen-1)):

                        corner_zero.add((r,c))

        q = deque(corner_zero)

        while q:

            curr_x, curr_y = q.popleft()

            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:

                nx,ny = curr_x+dx, curr_y+dy

                if 0<=nx<rlen and 0<=ny<clen and (nx,ny) not in visited:

                    if board[nx][ny] == 'O':
                        corner_zero.add((nx,ny))
                        q.append((nx,ny))
                        visited.add((nx,ny))


        for r in range(rlen):
            for c in range(clen):

                if (r,c) not in corner_zero:
                    board[r][c] = 'X'



