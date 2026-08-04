class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
         
        s = s.lower()
        t = t.lower()

        ch_check = [0]*26

        for i in range(len(s)):

            ch_check[ord(s[i])-ord('a')]+=1
            ch_check[ord(t[i])-ord('a')]-=1

        
        for c in ch_check:
            if c != 0:
                return False
        return True

