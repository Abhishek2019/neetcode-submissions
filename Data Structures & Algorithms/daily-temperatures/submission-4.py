class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stck = []


        out = [0 for _ in range(len(temperatures))]


        for idx, t in enumerate(temperatures):

            if not stck:
                stck.append((idx,t))

            else:

                while stck and t>stck[-1][1]:

                    prev_idx,prev_t = stck.pop()

                    out[prev_idx] = idx-prev_idx


                stck.append((idx,t))

                

        return out

            
        