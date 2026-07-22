class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        out = []
        candidates.sort()

        def dfs(i, curr_sum, curr_set):


            if target == curr_sum:
                out.append(curr_set.copy())
                return

            if i>=len(candidates) or curr_sum > target:
                return
            curr_set.append(candidates[i])
            curr_sum+=candidates[i]

            dfs(i+1, curr_sum, curr_set)
            
            curr_set.pop()
            curr_sum-=candidates[i]
            while i < len(candidates)-1 and candidates[i+1] == candidates[i]:
                i = i+1

            dfs(i+1, curr_sum, curr_set)





        dfs(0, 0, [])

        return out
