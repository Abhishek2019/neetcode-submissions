class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        
        need = Counter(s1)
        
        win = Counter()
        l=0

        for r,ch in enumerate(s2):
            win[ch]+=1

            while (r-l+1)>len(s1):
                win[s2[l]]-=1
                l+=1

            if win == need:
                return True

        return False