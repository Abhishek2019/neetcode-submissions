class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        n = len(s)

        max_len = 0
        max_seq = ''

        grid = [[0]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):

                if s[i] == s[j] and ( (j-i+1) <=3 or grid[i+1][j-1] == 1):

                    if j-i+1 > max_len:
                        max_len = j-i+1
                        max_seq = s[i:j+1]
                    
                    grid[i][j] = 1

        return max_seq

