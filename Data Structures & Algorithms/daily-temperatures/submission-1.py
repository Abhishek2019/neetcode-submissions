class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0 for _ in range(len(temperatures))]

        st = []
        for r in range(len(temperatures)):

            if not st:
                st.append((temperatures[r],r))
            
            else:
                while st and st[-1][0] < temperatures[r]:

                    ele,old_idx = st.pop()
                    res[old_idx] = r-old_idx
                
                st.append((temperatures[r],r))

        return res




        
        
        