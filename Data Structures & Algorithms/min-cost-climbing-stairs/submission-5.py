class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = {}
        def dfs(i):

            if i>=len(cost):
                return 0


            if i in dp:
                return dp[i]

            s1 = dfs(i+1)
            s2 = dfs(i+2)

            dp[i] = min(s1,s2)+cost[i] 
            return min(s1,s2)+cost[i]

        out = min(dfs(0),dfs(1))
        return out 
        