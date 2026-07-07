import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-i for i in nums]
        heapq.heapify(nums)

        count = 0

        while count <k:
            ans = -heapq.heappop(nums)
            count+=1

        return ans
        