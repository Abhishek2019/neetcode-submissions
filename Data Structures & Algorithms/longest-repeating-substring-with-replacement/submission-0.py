class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = [0]*26


        n = len(s)

        left = 0
        max_freq = 0
        best = 0

        for right in range(n):

            freq[ord(s[right]) - ord('A')]+=1

            max_freq = max(max_freq, freq[ord(s[right]) - ord('A')])

            if (right-left+1) - max_freq >k:

                freq[ord(s[left])-ord('A')]-=1

                left+=1
            
            best = max(best, right-left+1)

        return best



