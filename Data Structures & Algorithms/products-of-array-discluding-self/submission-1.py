class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pass1 = [nums[0], nums[0]]
        
        temp_out = nums[0]
        for i in range(2,len(nums)):

            pass1.append(nums[i-1]*temp_out)
            temp_out = nums[i-1]*temp_out

        print(pass1)

        nums2 = nums[::-1]
        pass2 = [nums2[0], nums2[0]]

        temp_out = nums2[0]
        for i in range(2,len(nums2)):

            pass2.append(nums2[i-1]*temp_out)
            temp_out = nums2[i-1]*temp_out

        print(pass2[::-1])

        pass2 = pass2[::-1]
        output = [pass2[0]]

        for i in range(1,len(pass1)-1):
            output.append(pass1[i]*pass2[i])

        output.append(pass1[-1])
        return output
