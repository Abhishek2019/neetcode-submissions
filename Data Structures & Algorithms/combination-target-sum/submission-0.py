class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        out = []

        def dfs(i,curr_arr,curr_sum):
            nonlocal out

            if curr_sum == target:
                out.append(curr_arr.copy())
                return

            if i >=len(nums):
                return

            if curr_sum > target:
                return

            dfs(i+1, curr_arr, curr_sum)

            curr_sum+=nums[i]
            curr_arr.append(nums[i])
            dfs(i,curr_arr, curr_sum)
            curr_arr.pop()
            curr_sum-=nums[i]


        dfs(0,[],0)
        return out