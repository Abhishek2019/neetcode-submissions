class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(i,n,dp):

            if i>=n:
                return 0
            if i in dp:
                return dp[i]
            s1 = dfs(i+1,n,dp)
            s2 = dfs(i+2,n,dp)

            dp[i] = max(s1, s2+nums[i]) 
            return max(s1, s2+nums[i])

        return max(dfs(0, len(nums)-1,{}), dfs(1,len(nums),{}))