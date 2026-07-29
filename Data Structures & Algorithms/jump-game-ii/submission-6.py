class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = {}
        def dfs(i):

            if i in dp:
                return dp[i]
            if i>=len(nums)-1:
                return 0

            if nums[i] == 0:
                return float("inf")

            s2 = float("inf")
            for j in range(1,nums[i]+1):

                s1 = 1+ dfs(i+j)

                s2 = min(s2,s1)

            dp[i] = s2
            return s2


        return dfs(0)