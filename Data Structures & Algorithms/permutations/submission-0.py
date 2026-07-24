class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        out = []
        used = set()
        def dfs(arr):

            nonlocal out

            #exit condn

            if len(arr) == len(nums):
                out.append(arr.copy())
                return

            for i in range(len(nums)):
                if i not in used:
                    
                    used.add(i)
                    arr.append(nums[i])
                    dfs(arr)
                    print(arr)
                    arr.pop()
                    used.remove(i)

        dfs([])

        return out