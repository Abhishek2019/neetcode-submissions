class Solution:
    def climbStairs(self, n: int) -> int:

        dp ={}
        
        def dfs(i):

            if i in dp:
                return dp[i]

            if i==n:
                return 1

            if i > n:
                return 0

            

            s1 = dfs(i+1)
            s2 = dfs(i+2)
            
            dp[i] = s1+s2
            return s1+s2

        return dfs(0)