class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)

        curr_out = True
        curr_reachable = n-1

        for i in range(n-2,-1,-1):

            if i+nums[i]>=curr_reachable:

                curr_reachable = i
                curr_out = True

            else:
                curr_out = False

        return curr_out
