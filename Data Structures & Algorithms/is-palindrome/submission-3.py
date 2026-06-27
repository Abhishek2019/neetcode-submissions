class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        left = 0
        right = n-1

        while left <= right:

            while left<=n-1 and not s[left].isalnum():
                left+=1
            
            while right>=0 and not s[right].isalnum():
                right-=1

            if left > right:
                return True
            
            print(s[left], s[right])
            if s[left].lower() == s[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True
        
        