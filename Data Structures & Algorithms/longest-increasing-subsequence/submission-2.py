class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = {}
        def dfs(prev, curr):

            s1 = 0

            if (prev, curr) in dp:
                return dp[(prev, curr)]
            if curr>=len(nums):
                return 0

            skip_curr = dfs(prev, curr+1)

            if prev == -1 or nums[curr] > nums[prev]:
                s1 = 1+dfs(curr, curr+1)
            
            dp[(prev, curr)] = max(skip_curr, s1)
            return dp[(prev, curr)]


        out = dfs(-1,0)
        return out