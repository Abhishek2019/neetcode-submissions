class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)

        out = [0]*n

        stack = []

        for i in range(n):

            print(stack)
            if not stack:
                stack.append((temperatures[i],i))
            
            else:

                while stack and temperatures[i] > stack[-1][0]:

                    x, idx = stack.pop()
                    out[idx] = i-idx
                
                stack.append((temperatures[i],i))
            
        return out

        

