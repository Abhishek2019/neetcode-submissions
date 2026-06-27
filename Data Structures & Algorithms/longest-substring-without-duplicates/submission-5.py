from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sliding_window = set()
        window = deque([])

        max_len = 0

        out = 0
        for ele in s:

            if ele not in sliding_window:

                sliding_window.add(ele)
                window.append(ele)

                out+=1

            else:

                while ele in sliding_window:
                    st_ele = window.popleft()
                    sliding_window.remove(st_ele)
                    out-=1

                sliding_window.add(ele)
                window.append(ele)
                out+=1

            max_len = max(max_len,out)
        return max_len
                