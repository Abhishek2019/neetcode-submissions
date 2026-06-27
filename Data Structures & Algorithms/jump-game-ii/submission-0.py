from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        l = r = 0  # current window of indices reachable with 'jumps' jumps

        while r < n - 1:
            farthest = r
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            jumps += 1

        return jumps
