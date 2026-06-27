class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def get_area(h,w):
            return h*w

        
        st = 0
        end = len(heights)-1

        out = -1

        while st<end:

            out = max(out,get_area(min(heights[st], heights[end]), end-st))

            if heights[st] > heights[end]:

                end-=1

            else:
                st+=1

        return out


