class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        target = 0
        if not nums:
            return []
        
        nums.sort()

        seen = set()

        n = len(nums)

        out = []
        for i in range(n):

            if nums[i] > 0:
                break

            
            if nums[i] not in seen:

                seen.add(nums[i])


                left = i+1
                right= n-1

                found_left = None
                found_right = None

                while left < right and left <=n-1 and right>=0:

                    total = nums[left]+nums[right]+nums[i]

                    if total == target:
                        out.append([nums[i], nums[left], nums[right]])
                        left_val = nums[left]
                        right_val = nums[right]

                        while left < right and nums[left] == left_val:
                            left += 1

                        while left < right and nums[right] == right_val:
                            right -= 1
                    
                    elif total < target:

                        left+=1
                    
                    else:
                        right -=1

        return out

                




                    









