class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def hours_req(rate):

            return sum([math.ceil(i/rate) for i in piles])
        r = max(piles)

        l = 1

        while l<r:

            mid = (l+r)//2


            if  hours_req(mid)>h:

                l = mid+1

            else:
                r = mid

            

        return r

