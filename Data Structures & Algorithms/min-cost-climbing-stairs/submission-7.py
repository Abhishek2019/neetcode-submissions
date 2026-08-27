class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)-1

        dp = {}
        def dfs(i):

            if i in dp:
                return dp[i]

            if i == n:
                return cost[-1]

            if i>n:
                return 0



            s1 = cost[i]+dfs(i+1)
            s2 = cost[i]+dfs(i+2)

            dp[i] = min(s1,s2)
            return dp[i]



        return min(dfs(0), dfs(1))