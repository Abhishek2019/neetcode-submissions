class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n ==1:
            return nums[0]

        dp = {}
        def dfs(i,c_n):


            if (i,c_n) in dp:
                return dp[(i,c_n)]
            if i>=c_n:
                return 0

            s1 = nums[i]+dfs(i+2,c_n)
            s2 = dfs(i+1,c_n)

            dp[(i,c_n)] =  max(s1,s2)

            return dp[(i,c_n)]

        return max(dfs(0,n-1),dfs(1,n))