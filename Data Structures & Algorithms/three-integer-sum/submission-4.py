class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        out = []
        nums = sorted(nums)
        for idx in range(len(nums)):

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            target = nums[idx]

            st = idx+1
            end = len(nums)-1

            while (st < end):
                if nums[st]+nums[end] == -target:

                    out.append([target, nums[st],nums[end]])
                    st+=1
                    end-=1
                    while st < end and nums[st] == nums[st - 1]:
                        st += 1

                    while st < end and nums[end] == nums[end + 1]:
                        end -= 1

                elif nums[st]+nums[end] > -target:

                    end-=1

                else:
                    st+=1

        return out         
            




        
