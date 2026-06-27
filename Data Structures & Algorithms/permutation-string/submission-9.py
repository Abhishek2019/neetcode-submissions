

from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_map = Counter(s1)
        s2_map = defaultdict(int)

        l = 0

        for r in range(len(s2)):
            s2_map[s2[r]] += 1

            if r - l + 1 > len(s1):
                s2_map[s2[l]] -= 1

                if s2_map[s2[l]] == 0:
                    del s2_map[s2[l]]

                l += 1

            if s2_map == s1_map:
                return True

        return False
