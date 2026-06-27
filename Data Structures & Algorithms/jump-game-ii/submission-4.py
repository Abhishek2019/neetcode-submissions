class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)

        l=r=0
        count = 0

        while r<n-1:

            max_reach = float("-inf")

            for i in range(l,r+1):

                max_reach = max(max_reach, i+nums[i])
            l = r+1
            r = max_reach
            count+=1
        
        return count
