from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = Counter(t)
        req = len(need)

        win = Counter()

        l = 0
        have = 0

        min_len = float("inf")
        min_l = 0
        min_r = 0

        for r, ch in enumerate(s):

            win[ch] += 1

            # This character requirement is now satisfied
            if ch in need and win[ch] == need[ch]:
                have += 1

            # All requirements satisfied
            while have == req:

                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_l = l
                    min_r = r

                # Removing s[l] will break this requirement
                if s[l] in need and win[s[l]] == need[s[l]]:
                    have -= 1

                win[s[l]] -= 1
                l += 1

        if min_len == float("inf"):
            return ""

        return s[min_l:min_r + 1]