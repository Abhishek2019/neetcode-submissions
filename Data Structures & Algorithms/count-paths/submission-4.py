class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}
        def dfs(x,y):

            if (x,y) in dp:
                return dp[(x,y)]
            
            if x>=m or y>=n:
                return None
    
            if x == (m-1) and y == (n-1):
                return 1
            
            s1 = dfs(x+1,y)
            s2 = dfs(x,y+1)
            
            if not s1:
                s1 = 0
            
            if not s2:
                s2 = 0
            
            dp[(x,y)] = s1+s2
            return dp[(x,y)]

        out = dfs(0,0)
        return out

        


