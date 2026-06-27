class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        

        def helper(arr):

            arr.append(0)
            n = len(arr)

            for i in range(n-3,-1,-1):

                arr[i] = max(arr[i]+arr[i+2], arr[i+1])

            return max(arr[0], arr[1])

        return max(helper(nums[1::]), helper(nums[:-1]))