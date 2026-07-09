class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp_pal = {}
        def is_palindrome(l,r):

            if l<=r:
                if (l,r) in dp_pal:
                    return dp_pal[(l,r)]
                if l == r:
                    dp_pal[(l,r)] = True
                    return True
                
                if (l+1 == r) and s[l] == s[r]:
                    dp_pal[(l,r)] = True
                    return True
                
                if (s[l] == s[r]) and is_palindrome(l+1,r-1):
                    dp_pal[(l,r)] = True
                    return True
                else:
                    dp_pal[(l,r)] = False
                    return False
            return None

        out_str = ""
        visited = set()
        def dfs(l,r):
            nonlocal out_str

            if l>r:
                return
            if (l,r) in visited:
                return
            visited.add((l,r))
            if is_palindrome(l,r):
                curr = s[l:r+1]

                if len(curr) > len(out_str):
                    out_str = curr
                return

            dfs(l,r-1)
            dfs(l+1,r)

        dfs(0,len(s)-1)
        return out_str





