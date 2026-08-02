from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        c = Counter(s)

        pool_freq = float("inf")
        curr_set = set()
        final = []
        prev_i = 0
        for i in range(len(s)):

            ele = s[i]
            if pool_freq == 0:
                final.append(i-prev_i)
                curr_set = set()
                prev_i = i

            if not curr_set:
                curr_set.add(ele)
                pool_freq=c[ele]-1
            
            else:
                if ele in curr_set:
                    pool_freq-=1

                else:
                    curr_set.add(ele)
                    pool_freq+=c[ele]-1

        final.append(len(s)-prev_i)        

        return final


        
