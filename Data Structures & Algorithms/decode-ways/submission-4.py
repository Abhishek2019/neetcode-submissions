class Solution:
    def numDecodings(self, s: str) -> int:
        
        end = len(s)-1
        dp = {}
        def dfs(start):

            if start > end:
                return 1

            if start in dp:
                return dp[start]
            
            if int(s[start]) == 0:
                dp[start] = 0
                return 0
            
            s1 = dfs(start+1)

            if 10<=int(s[start:start+2]) <= 26:
                s2 = dfs(start+2)
            else:
                s2 = 0

            dp[start] = s1+s2
            return s1+s2



        out = dfs(0)
        return out