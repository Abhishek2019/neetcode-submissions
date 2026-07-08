class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}
        def dfs(i):

            if i>=len(nums):
                return 0
            
            if i in dp:
                return dp[i]

            s1 = dfs(i+1)
            s2 = dfs(i+2)
            
            dp[i] = max(nums[i]+s2, s1) 
            return max(nums[i]+s2, s1)
            

        out = dfs(0)
        return out