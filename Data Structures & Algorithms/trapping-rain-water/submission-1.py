class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n-1

        left_max = height[0]
        right_max = height[-1]

        water = 0

        while left < right:

            if height[left] > left_max:
                left_max = height[left]
            
            if height[right] > right_max:
                right_max = height[right]
            
            if left_max < right_max:
                curr_water=min(left_max, right_max)-height[left]

                if curr_water >0:
                    water+=curr_water
                
                left+=1


            else:

                curr_water=min(left_max, right_max)-height[right]

                if curr_water >0:
                    water+=curr_water
                
                right-=1

        return water






        

