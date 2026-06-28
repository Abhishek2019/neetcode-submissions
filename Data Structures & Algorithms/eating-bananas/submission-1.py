import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        k_st = 1
        k_end = max(piles)

        def get_hours(curr_k):
            return sum([math.ceil(i/curr_k) for i in piles])

        answer = 0
        while k_st <= k_end:

            mid_k = (k_st+k_end)//2
            mid_h = get_hours(mid_k)
            if  mid_h <= h:
                answer = mid_k
                k_end = mid_k-1
            else:
                k_st = mid_k +1

        return answer

        