
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = 0
        r = 0

        curr_max = deque([])

        best = float("-inf")
        out = []

        while r< len(nums):

            while (r-l+1) <=k:

                if not curr_max:
                    curr_max.append(nums[r])
                
                else:
                    while curr_max and curr_max[-1] < nums[r]:
                        curr_max.pop()
                    
                    curr_max.append(nums[r])

                
                r+=1

            out.append(curr_max[0])
            while (r-l+1) >k:

                if curr_max[0] == nums[l]:
                    curr_max.popleft()
                l+=1
        return out

        