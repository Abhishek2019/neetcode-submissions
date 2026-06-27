from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        map = defaultdict(int)

        l = 0

        ans = 0

        for r in range(len(s)):

            map[s[r]]+=1

            
            while (r-l+1)-max(map.values()) > k:
                
                map[s[l]]-=1
                l+=1

            ans = max(ans,(r-l+1))

        return ans
            






