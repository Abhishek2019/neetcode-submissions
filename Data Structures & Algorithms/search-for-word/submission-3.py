class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        visited = set()
        def dfs(x,y,i):
            
            if i == len(word):
                return True
            if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
                return False          
            if board[x][y] != word[i]:
                return False

            if(x,y) in visited:
                return False



            visited.add((x,y))
            found = (

                dfs(x+1,y,i+1) or
                dfs(x,y+1,i+1) or
                dfs(x-1,y,i+1) or
                dfs(x,y-1,i+1)  
            )

            visited.remove((x,y))

            return found

        for r in range(len(board)):
            for c in range(len(board[0])):

                if dfs(r,c,0):
                    return True

        return False