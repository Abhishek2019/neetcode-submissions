class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        pass1 = [nums[0],nums[0]]
        pass2 = []

        n = len(nums)

        for i in range(2,n):
            pass1.append(nums[i-1]*pass1[i-1])

        pass2_prev = 1
        for j in range(n-1, -1, -1):

            if j == n-1 or j == n-2:
                pass2.append(nums[-1])
            
            else:
                pass2.append(nums[j+1]*pass2[pass2_prev])
                pass2_prev+=1
        
        pass2 = pass2[::-1]

        print(pass1)
        print(pass2)

        c = 0
        out = []

        for x,y in zip(pass1, pass2):

            if c == 0:
                out.append(y)
            elif c == n-1:
                out.append(x)
            else:
                out.append(x*y)

            c+=1

        return out
              






