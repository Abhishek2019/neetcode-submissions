from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)


        for s in strs:

            sig = [0]*26

            for ch in s:

                sig[ord(ch)-ord('a')]+=1

            
            d[tuple(sig)].append(s)

        
        return list(d.values())
        
        