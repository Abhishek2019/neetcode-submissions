from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0

        cnt = defaultdict(int)

        maxf,best = 0,0


        for r,ch in enumerate(s):

            cnt[ch]+=1
            maxf = max(maxf, cnt[ch])

            while (r-l+1) - maxf >k:

                cnt[s[l]]-=1
                l+=1

            best = max(best,(r-l+1))

        return best







        