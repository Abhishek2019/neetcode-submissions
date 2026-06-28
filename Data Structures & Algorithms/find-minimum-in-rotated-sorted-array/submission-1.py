class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l =0
        r = len(nums)-1
        ans = 0
        while l<=r:
            
            mid = (l+r)//2

            ans = nums[mid]

            print(ans)

            if ans > nums[r]:
                l = mid+1
            elif ans < nums[r]:
                r = mid
            else:
                return ans

        return ans


                



            