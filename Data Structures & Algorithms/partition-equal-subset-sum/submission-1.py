class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        ref_sum = sum(nums)
        dp = {}

        def dfs(i,curr_sum):

            if (i,curr_sum) in dp:
                return dp[(i,curr_sum)]

            if i>=len(nums):
                return False

            
            if curr_sum == ref_sum-curr_sum:
                dp[(i,curr_sum)] = True
                return True

            if curr_sum > (ref_sum-curr_sum):
                dp[(i,curr_sum)] = False
                return False
            

            s1 = dfs(i+1, curr_sum)

            if s1:
                return True
            curr_sum+=nums[i]
            s2 = dfs(i+1, curr_sum)

            curr_sum-=nums[i]

            if s1 or s2:
                return True

            dp[(i,curr_sum)] = False
            return False 

        out = dfs(0,0)

        return out
