class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[-1]
        curr_min = nums[-1]
        max_prod = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]

            next_max = curr_max
            next_min = curr_min

            curr_max = max(
                num,
                num * next_max,
                num * next_min
            )

            curr_min = min(
                num,
                num * next_max,
                num * next_min
            )

            max_prod = max(max_prod, curr_max)

        return max_prod