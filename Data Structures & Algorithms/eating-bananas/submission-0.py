import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)

        if h < n:
            return -1

        left = 1

        right = max(piles)

        while left < right:

            mid = (left+right)//2
            check = sum([math.ceil(i/mid) for i in piles])

            if check <=h:
                right = mid
            else:
                left = mid+1
        return left
                
            

