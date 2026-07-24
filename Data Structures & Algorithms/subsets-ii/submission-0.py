class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        out = []

        nums.sort()
        
        def dfs(i, arr):

            nonlocal out

            # exit condn

            if i>=len(nums):
                out.append(arr.copy())
                return

            # include

            arr.append(nums[i])
            dfs(i+1,arr)
            arr.pop()

            # skip
            while i<len(nums)-1 and nums[i] == nums[i+1]:
                i = i+1
            dfs(i+1,arr)


        dfs(0,[])
        return out