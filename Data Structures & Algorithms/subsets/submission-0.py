class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        out = []

        def dfs(i,arr):
            
            nonlocal out
            if i>=len(nums):
                out.append(arr.copy())
                return
            
            dfs(i+1,arr)
            
            arr.append(nums[i])

            dfs(i+1,arr)

            arr.pop()


        dfs(0,[])

        return out