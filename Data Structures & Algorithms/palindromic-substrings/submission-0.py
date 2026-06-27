class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        c = 0

        grid = [[0]*n for _ in range(n)]

        for i in range(n-1,-1,-1):

            for j in range(i,n):

                if s[i] == s[j] and ( (j-i+1 <=3) or grid[i+1][j-1] == 1):
                    c+=1

                    grid[i][j] = 1 

        return c
        