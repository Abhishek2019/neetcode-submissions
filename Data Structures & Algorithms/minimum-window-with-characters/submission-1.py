from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        need = Counter(t)
        need_unique = len(need)
        
        window = defaultdict(int)
        have = 0
        
        res_left = 0
        res_right = 0
        res_len = float("inf")
        
        left = 0

        for right, ch in enumerate(s):
            if ch in need:
                window[ch] += 1

                if window[ch] == need[ch]:
                    have += 1

            while have == need_unique:
                window_len = right - left + 1
                if window_len < res_len:
                    res_len = window_len
                    res_left = left
                    res_right = right
                
                left_char = s[left]
                if left_char in need:
                    window[left_char] -= 1

                    if window[left_char] < need[left_char]:
                        have -= 1
                left += 1
        
        return "" if res_len == float("inf") else s[res_left:res_right + 1]
