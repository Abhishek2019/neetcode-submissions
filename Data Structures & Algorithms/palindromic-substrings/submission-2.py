class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        def is_palindrome(l,r):
            temp = 0
            while l <=r and l>=0 and r<len(s):

                if s[l] == s[r]:
                    temp+=1
                    l-=1
                    r+=1
                else:
                    return temp
            return temp


        
        for ch in range(len(s)):
            st1 = is_palindrome(ch,ch)
            if ch<len(s)-1:
                st2 = is_palindrome(ch,ch+1)
            else:
                st2=0

            
            count += (st1+st2)


        return count