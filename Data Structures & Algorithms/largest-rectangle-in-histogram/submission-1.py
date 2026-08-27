class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []

        max_area = 0

        for idx,h in enumerate(heights):

            start = idx

            while stack and h < stack[-1][1]:

                prev_idx,prev_height = stack.pop()
                curr_height = prev_height
                curr_width = idx-prev_idx

                max_area = max(max_area, curr_height*curr_width)

                start = prev_idx

            stack.append((start,h))

        
        for remain_idx,remain_height in stack:

            max_area = max(max_area, remain_height*(len(heights)-remain_idx))

        return max_area


        


        