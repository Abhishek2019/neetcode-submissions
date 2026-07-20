class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        if (len(s1) + len(s2)) !=len(s3):
            return False
        dp = {}
        def dfs(i,j):
            
            if (i,j) in dp:
                return dp[(i,j)]
            if i == len(s1) and j==len(s2):
                return True            
            k = i+j
            i_found, j_found = False, False
            if i < len(s1) and s1[i] == s3[k]:

                i_found = dfs(i+1,j)

            if j < len(s2) and s2[j] == s3[k]:

                j_found = dfs(i,j+1)

            # if s1[i] != s3[k] and  s2[j] != s3[k]:
            #     return False

            dp[(i,j)] = i_found or j_found
            return dp[(i,j)]

        out = dfs(0,0)
        return out