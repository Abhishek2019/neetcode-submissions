class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        def dfs(i, curr_sum):
            
            if (i,curr_sum) in dp:
                return dp[(i,curr_sum)]
           
            if curr_sum == target and i >= (len(nums)):
                return 1

            if i >=len(nums):
                return 0 


            # s1 = dfs(i+1,curr_sum)
            s2 = dfs(i+1, curr_sum-nums[i])
            s3 = dfs(i+1, curr_sum+nums[i])
            
            dp[(i,curr_sum)] = s2+s3
            return s2+s3

        return dfs(0,0)

