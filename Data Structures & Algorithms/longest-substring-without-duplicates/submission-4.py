from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        window = deque([])
        seen = set()

        n = len(s)

        out = 0

        for i in range(n):

            if not seen:
                window.append(s[i])
                seen.add(s[i])
            elif s[i] in seen:

                if len(window) > out:
                    out = len(window)

                while window and window[0] != s[i]:

                    x = window.popleft()
                    seen.remove(x)
                
                if window:
                    x = window.popleft()
                    seen.remove(x)
                
                window.append(s[i])
                seen.add(s[i])

            else:
                seen.add(s[i])
                window.append(s[i])

        
        if len(window) > out:
            out = len(window)
        return out