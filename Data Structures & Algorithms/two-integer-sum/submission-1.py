class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i in range(len(nums)):

            delta = target - nums[i]

            if delta in d:
                return [d[delta], i]
            
            else:

                d[nums[i]] = i

        