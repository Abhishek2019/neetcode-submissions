class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}
        def dfs(i):

            if i in dp:
                return dp[i]
            if i>=len(nums):
                return 0

            s1 = nums[i]+dfs(i+2)

            s2 = dfs(i+1)

            dp[i] = max(s1,s2)
            return dp[i]

        return dfs(0)